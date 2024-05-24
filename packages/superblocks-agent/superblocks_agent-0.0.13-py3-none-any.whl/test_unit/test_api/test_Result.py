import unittest

from superblocks_types.api.v1.event_pb2 import Event, Output
from superblocks_types.api.v1.service_pb2 import StreamResponse
from superblocks_types.common.v1.errors_pb2 import Error

from superblocks_agent._util.convert import to_protobuf_value
from superblocks_agent.api import Result


class TestResult(unittest.TestCase):
    def test_from_proto_stream_responses__empty_list(self):
        actual = Result.from_proto_stream_responses([])
        self.assertEqual(Result(events=[], output=None), actual)

    def test_from_proto_stream_responses__with_errors(self):
        output = Output(result=to_protobuf_value({"foo": "bar"}))
        end_event = Event(name="end_event", end=Event.End(output=output))
        errors = [Error(message="some error")]
        response_event = Event(
            name="response_event", response=Event.Response(last="end_event", errors=errors)
        )
        actual = Result.from_proto_stream_responses(
            [StreamResponse(event=end_event), StreamResponse(event=response_event)]
        )
        expected = Result(events=[end_event, response_event], errors=errors, output=output)
        self.assertEqual(expected, actual)

    def test_from_proto_stream_responses__without_error(self):
        output = Output(result=to_protobuf_value({"foo": "bar"}))
        end_event = Event(name="end_event", end=Event.End(output=output))
        response_event = Event(
            name="response_event", response=Event.Response(last="end_event", errors=[])
        )
        actual = Result.from_proto_stream_responses(
            [StreamResponse(event=end_event), StreamResponse(event=response_event)]
        )
        expected = Result(events=[end_event, response_event], errors=[], output=output)
        self.assertEqual(expected, actual)

    def test_from_proto_stream_responses__no_matching_response_event_found(self):
        output = Output(result=to_protobuf_value({"foo": "bar"}))
        end_event = Event(name="end_event", end=Event.End(output=output))
        response_event = Event(
            name="response_event", response=Event.Response(last="i dont match anything", errors=[])
        )

        with self.assertRaises(Exception) as context:
            Result.from_proto_stream_responses(
                [StreamResponse(event=end_event), StreamResponse(event=response_event)]
            )
        self.assertEqual(
            "no matching event found for block 'i dont match anything'", str(context.exception)
        )
