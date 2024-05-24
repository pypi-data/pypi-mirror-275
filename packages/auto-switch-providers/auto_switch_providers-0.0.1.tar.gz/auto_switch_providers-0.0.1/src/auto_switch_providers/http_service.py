from json import dumps
import requests


class HttpService(object):
    def __init__(
        self,
        config=None,
        base_url: str = None,
        default_headers=None,
        endpoints=None,
    ) -> None:
        self.config = config
        self.base_url = base_url if base_url is not None else ""
        self.default_headers = default_headers if default_headers is not None else {}
        self.endpoints = endpoints if endpoints is not None else {}

    def _request(
        self,
        endpoint: str,
        method: str = "GET",
        params: dict = None,
        body: dict = None,
        headers: dict = None,
        timeout=10,
        url_params_format=None,
    ):
        endpoint = self.endpoints.get(endpoint) or endpoint
        if url_params_format:
            endpoint = endpoint.format(**url_params_format)
        headers = (
            {**self.default_headers, **headers} if headers else self.default_headers
        )
        url = self.base_url + (endpoint or "/")
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=body,
            timeout=timeout,
        )
        return response

    def request(
        self,
        endpoint: str,
        method: str = "GET",
        params: dict = None,
        body: dict = None,
        headers: dict = None,
        timeout=10,
        status_force_list=None,
        total=3,
        url_params_format=None,
    ):
        if status_force_list is None:
            status_force_list = []

        endpoint = self.endpoints.get(endpoint) or endpoint
        if url_params_format:
            endpoint = endpoint.format(**url_params_format)

        params_str = " - " + dumps(params) if params else ""

        for _ in range(total):
            try:
                log_endpoint = self.base_url + (endpoint or "/")
                response = self._request(
                    endpoint,
                    method=method,
                    params=params,
                    body=body,
                    headers=headers,
                    timeout=timeout,
                )

                if response.status_code in status_force_list:
                    print(
                        f"✅ [{response.elapsed.total_seconds() if response else None}s] {log_endpoint}:{log_endpoint} - retrying... ({_+1}) (code: wrong status_code)"
                    )
                    continue

                if response.status_code == 400:
                    print(
                        f"🚸 [{timeout if timeout else None}s] {method}: {log_endpoint}:{log_endpoint} - stopped ({_+1}) (code: HTTPError{params_str}"
                    )
                else:
                    print(
                        f"✅ [{response.elapsed.total_seconds() if response else None}s] GET: {log_endpoint}:{log_endpoint}{params_str}"
                    )

                return response
            except requests.exceptions.Timeout:
                print(
                    f"⛔️ [{timeout if timeout else None}] {method}: {log_endpoint}:{log_endpoint} - retrying... ({_+1}) (code: Timeout){params_str}"
                )
                continue
            except requests.exceptions.ConnectionError:
                print(
                    f"⛔️ [{timeout if timeout else None}] {method}: {log_endpoint}:{log_endpoint} - stopped ({_+1}) (code: ConnectionError{params_str}"
                )
                pass

        return None
