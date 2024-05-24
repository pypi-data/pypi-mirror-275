from json import dumps, loads
from os import path, walk
from typing import List
from jinja2 import Environment, FileSystemLoader
from marshmallow import EXCLUDE, Schema, fields
from requests import Response
from yaml import safe_load

from .http_service import HttpService
from .utils.helpers import merge_child, nested_dict_get


class AutoSwitchProviders:
    def __init__(self, template_dir: str, config: dict = {}) -> None:
        self.template_dir = template_dir
        self.providers = []
        self.config = config or {}

        if self.template_dir:
            self._discover_templates()

    def process(self, data: dict):
        if not self.providers or len(self.providers) == 0:
            print("⛔️ Empty provider!")
            return None

        process_response = None
        for provider in self.providers:
            try:
                template: dict = safe_load(provider.get("template").render(data))
            except Exception as e:
                print(f"⛔️ error - {dumps(data)}")
                continue

            template_type = template.get("type") or None
            template_default_config: dict = (
                self.config[template_type] if template_type else {}
            )
            template_http_service_default_config: dict = template_default_config.get(
                "http_service", {}
            )
            template_request_config = template.get("request", {})
            default_keys = template_http_service_default_config.keys()
            for default_key_item in default_keys:
                if default_key_item in template_request_config:
                    template_request_config[default_key_item] = {
                        **template_request_config.get(default_key_item),
                        **template_http_service_default_config[default_key_item],
                    }
                else:
                    template_request_config[default_key_item] = (
                        template_http_service_default_config[default_key_item]
                    )

            if "pagination" in template:
                process_response = self._paginate(
                    request=dict(
                        method=template.get("method") or "GET",
                        endpoint=template.get("url") or "/",
                        timeout=template.get("timeout", 10),
                        params=template_request_config.get("params") or None,
                        body=template_request_config.get("body") or None,
                        headers=template_request_config.get("headers") or None,
                    ),
                    config=template.get("pagination"),
                    template=template,
                )
                if process_response:
                    break
            else:
                process_response = self._single(
                    request=dict(
                        method=template.get("method") or "GET",
                        endpoint=template.get("url") or "/",
                        timeout=template.get("timeout", 10),
                        params=template_request_config.get("params") or None,
                        body=template_request_config.get("body") or None,
                        headers=template_request_config.get("headers") or None,
                    ),
                    template=template,
                )
                if process_response:
                    break

        return process_response

    def _single(self, request: dict, template: dict):
        response = self._process(request, template)
        if "response" in response and response is not None:
            return response.get("response", [])
        return None

    def _paginate(self, request: dict, config: dict, template: dict):
        next_page_type = config.get("request_field", {}).get("type")
        next_page_key = config.get("request_field", {}).get("target")

        next_cursor = None
        has_more = True

        items = []
        page = 0

        while page < config.get("total_page", 10) and has_more == True:
            page = page + 1
            if next_cursor:
                if next_page_type in request and next_page_key in request.get(
                    next_page_type
                ):
                    request[next_page_type][next_page_key] = next_cursor

            response = self._process(request, template, config)
            if "response" in response and response is not None:
                items.append(response.get("response"))
            if "has_more" in response:
                has_more = response.get("has_more")
            if "next_cursor" in response:
                next_cursor = response.get("next_cursor")

        if len(items) == 0 or not items:
            return None

        if "merge_field" not in config:
            return items

        return merge_child(items)

    def _process(self, request: dict, template: dict, pagination_config: dict = None):
        http_service = HttpService()
        response = http_service.request(**request)
        cursor_response_target = (
            pagination_config.get("response_field") if pagination_config else None
        )
        next_cursor = None
        has_more = None
        process_response = None

        # Response config
        response_config: dict = template.get("response")
        if not response_config:
            return response

        response_type = response_config.get("type")
        if response_type != "text":
            response_json = (
                response.json()
                if isinstance(response, Response)
                else loads(response.get("text"))
            )

            if cursor_response_target:
                next_cursor = (
                    nested_dict_get(response_json, cursor_response_target) or None
                )
                has_more = False if not next_cursor else True

            # Check errors
            if "$errors" in response_config:
                has_error: dict = self._check_response_errors(
                    response_config.get("$errors"), response
                )
                if has_error.get("status") is False:
                    return {
                        "code": 0,
                        "message": response_config.get(has_error.get("reason_field")),
                    }

            if "$schema" in response_config:
                response_json = self._transform_with_response_schema(
                    response_config.get("$schema"),
                    response_json,
                )
                process_response = response_json
            else:
                process_response = response_json

        return {
            "response": process_response,
            "has_more": has_more,
            "next_cursor": next_cursor,
        }

    @staticmethod
    def _transform_with_response_schema(schema_template: dict, response):
        schema_dict = {}
        for key in schema_template.keys():
            cur_schema_value: dict = schema_template[key]
            cur_schema_value_type: str = cur_schema_value.get("type", key)
            cur_schema_value_key: str = cur_schema_value.get("target", key)
            cur_schema_value_default: str = cur_schema_value.get("default", None)

            if cur_schema_value_type == "list":
                list_item_schema: dict = cur_schema_value.get("$schema", {})
                item_schema_dict = {}
                for i_key in list_item_schema.keys():
                    cur_schema_item_value: dict = list_item_schema[i_key]
                    cur_schema_item_key: str = cur_schema_item_value.get("target")
                    cur_schema_item_default: str = cur_schema_item_value.get("default")
                    item_schema_dict.update(
                        {
                            i_key: fields.Raw(
                                data_key=cur_schema_item_key,
                                missing=cur_schema_item_default,
                            )
                        }
                    )

                schema_dict.update(
                    {
                        key: fields.List(
                            cls_or_instance=fields.Nested(
                                Schema(unknown=EXCLUDE).from_dict(item_schema_dict),
                                unknown=EXCLUDE,
                            ),
                            data_key=cur_schema_value_key,
                            missing=cur_schema_value_default,
                        )
                    }
                )
            else:
                schema_dict.update(
                    {
                        key: fields.Raw(
                            data_key=cur_schema_value_key,
                            missing=cur_schema_value_default,
                        )
                    }
                )

        schema = Schema(unknown=EXCLUDE).from_dict(schema_dict)
        transformed_response = schema().load(response, unknown=EXCLUDE)
        return transformed_response

    @staticmethod
    def _check_response_errors(schemas: list, response):
        result = {}
        for err_schema in schemas:
            if "if" in err_schema and "then" in err_schema:
                if_cond = err_schema.get("if")
                then_cond = err_schema.get("then")
                response_status_code = (
                    response.get("status_code")
                    if not isinstance(response, Response)
                    else response.status_code
                )
                if "status_code" in if_cond and response_status_code == if_cond.get(
                    "status_code"
                ):
                    result = {
                        "status": False,
                        "reason_field": then_cond.get("reason_field", ""),
                    }
                    break

        return result

    def _discover_templates(self):
        filenames: List[str] = next(walk(self.template_dir), (None, None, []))[2]

        if len(filenames) > 0:
            jinja2_env = Environment(loader=FileSystemLoader(self.template_dir))
            self.providers = list(
                map(
                    lambda x: {
                        "_file": x,
                        "id": path.splitext(x)[0],
                        "template": jinja2_env.get_template(x),
                    },
                    filter(lambda x: x.endswith(".yaml"), filenames),
                )
            )
