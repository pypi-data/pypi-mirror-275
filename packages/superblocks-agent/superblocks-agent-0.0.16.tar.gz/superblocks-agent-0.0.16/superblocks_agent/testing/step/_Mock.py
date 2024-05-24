from __future__ import annotations

from typing import Optional

from superblocks_types.api.v1.service_pb2 import Mock as ProtoMock

from superblocks_agent._util.convert import Mock_, to_protobuf_value
from superblocks_agent._util.generate import get_unique_id_for_object
from superblocks_agent.testing.step import Params
from superblocks_agent.types.mock import JsonValue, MockCallable, WhenCallable, is_json_value


class Mock:
    def __init__(self, params: Optional[Params] = None, *, when: Optional[WhenCallable] = None):
        self.__on_params = params
        self.__when_callable = when
        self.__return_value = None
        self.__return_callable = None

    def get_return_value(self) -> Optional[dict]:
        return self.__return_value

    def get_return_callable(self) -> Optional[MockCallable]:
        return self.__return_callable

    def get_when_callable(self) -> Optional[WhenCallable]:
        return self.__when_callable

    # we use "return_" as is recommended by PEP 8: https://peps.python.org/pep-0008/#descriptive-naming-styles
    def return_(self, value: JsonValue | MockCallable) -> Mock:
        # NOTE: (joey) i don't know if there's an easy way to validate the function signature
        if callable(value):
            self.__return_callable = value
        elif is_json_value(value):
            self.__return_value = value
        else:
            raise ValueError(f"invalid type for return: '{type(value)}'")
        return self

    def to_proto_on(self) -> Optional[ProtoMock.On]:
        mock_on = None
        if self.__on_params is not None:
            mock_on = ProtoMock.On()
            mock_on.static.CopyFrom(self.__on_params.to_proto_params())
        if self.__when_callable is not None:
            mock_on = ProtoMock.On() if mock_on is None else mock_on
            mock_on.dynamic = get_unique_id_for_object(self.__when_callable)
        return mock_on

    def to_proto_return(self) -> Optional[Mock.Return]:
        mock_return = None
        if self.__return_value is not None or self.__return_callable is not None:
            mock_return = ProtoMock.Return()
            if self.__return_value is not None:
                mock_return.static.CopyFrom(to_protobuf_value(self.__return_value))
            elif self.__return_callable is not None:
                # should be type type_.mock.WhenCallable
                mock_return.dynamic = get_unique_id_for_object(self.__return_callable)
        return mock_return

    def to_proto_mock(self) -> Mock:
        return Mock_(on=self.to_proto_on(), return_=self.to_proto_return())


def on(params: Optional[Params] = None, *, when: Optional[WhenCallable] = None) -> Mock:
    return Mock(params=params, when=when)
