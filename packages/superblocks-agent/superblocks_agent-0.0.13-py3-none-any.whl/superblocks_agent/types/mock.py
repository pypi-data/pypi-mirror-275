from __future__ import annotations

from typing import Callable, Union

from superblocks_agent.testing.step import Params

JsonValue = Union[str, float, int, bool, None, "JsonObject", "JsonArray"]
JsonObject = dict[str, JsonValue]
JsonArray = list[JsonValue]

# when {these params}
WhenCallable = Callable[[Params], bool]

# when {these params} return {this value}
MockCallable = Callable[[Params], JsonValue]
