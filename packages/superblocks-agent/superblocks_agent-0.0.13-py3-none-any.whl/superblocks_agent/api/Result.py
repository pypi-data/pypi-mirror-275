# TODO: (joey) some of these imports are weird
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from superblocks_types.api.v1.event_pb2 import Event, Output
from superblocks_types.api.v1.service_pb2 import StreamResponse
from superblocks_types.common.v1.errors_pb2 import Error

from superblocks_agent._util.convert import from_protobuf_value

# from superblocks_agent.types.mock import JsonValue
# TODO: (joey) make json value work


@dataclass(kw_only=True)
class Result:
    events: list[Event] = field(default_factory=list)
    errors: list[Error] = field(default_factory=list)
    output: Optional[Output] = None

    def get_result(self) -> any:
        val = None
        if self.output is not None:
            val = from_protobuf_value(self.output.result)
        return val

    def get_block_output_value(self, name: str) -> any:
        val = None
        for event in self.events:
            if event.HasField("end") and event.name == name:
                val = from_protobuf_value(event.end.output.result)
                break
        return val

    @staticmethod
    def from_proto_stream_responses(stream_responses: list[StreamResponse]) -> Result:
        events = []
        errors = []
        output = None
        output_block_name = None

        block_name_to_output_map = {}

        for stream_response in stream_responses:
            events.append(stream_response.event)
            # check if this event holds the output
            if stream_response.event.HasField("response"):
                output_block_name = stream_response.event.response.last
                errors = stream_response.event.response.errors
            elif stream_response.event.HasField("end"):
                block_name_to_output_map[
                    stream_response.event.name
                ] = stream_response.event.end.output

        # find "response" event by name
        output = block_name_to_output_map.get(output_block_name)
        if output_block_name is not None and output is None:
            raise Exception(f"no matching event found for block '{output_block_name}'")

        return Result(events=events, errors=errors, output=output)
