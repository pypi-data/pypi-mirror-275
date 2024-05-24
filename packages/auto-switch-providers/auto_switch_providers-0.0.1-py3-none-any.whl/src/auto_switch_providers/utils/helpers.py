import functools


def nested_dict_get(dictionary, dotted_key):
    keys = dotted_key.split(".")
    return functools.reduce(
        lambda d, key: (
            d[int(key)] if isinstance(d, list) else d.get(key) if d else None
        ),
        keys,
        dictionary,
    )


def merge_child(raw_dict: dict):
    return {k: [d.get(k) for d in raw_dict] for k in set().union(*raw_dict)}
