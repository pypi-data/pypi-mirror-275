from __future__ import annotations

from typing import Callable, Union

from superblocks_agent.testing.step import Params

JsonValue = Union[str, float, int, bool, None, "JsonObject", "JsonArray"]
JsonObject = dict[str, JsonValue]
JsonArray = list[JsonValue]


# NOTE: (joey) since we are using ForwardRefs in our Union type, we can't use isinstance cleanly.
# this function is the cleanest way i can think of for now
# SOURCES:
# https://stackoverflow.com/questions/76106117/python-resolve-forwardref
# https://stackoverflow.com/questions/45957615/how-to-check-a-variable-against-union-type-during-runtime
def is_json_value(value: any) -> bool:
    if isinstance(value, (str, float, int, bool)) or value is None:
        return True
    elif isinstance(value, dict):
        return all(isinstance(k, str) and is_json_value(v) for k, v in value.items())
    elif isinstance(value, list):
        return all(is_json_value(i) for i in value)
    return False


# when {these params}
WhenCallable = Callable[[Params], bool]

# when {these params} return {this value}
MockCallable = Callable[[Params], JsonValue]
