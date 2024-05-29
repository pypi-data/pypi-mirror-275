import queue

import grpc
from superblocks_types.api.v1.service_pb2 import StreamResponse

from superblocks_agent.client.Config import Config
from superblocks_agent.types._client import TwoWayStreamResponseHandler


class Client:
    """
    Used for connecting to the Superblocks Agent.
    """

    def __init__(self, config: Config):
        """
        Args:
            config (Optional[superblocks_agent.client.Config]): The Client configuration.
        """
        self.config = config
        self.__channel = None

    def close(self) -> None:
        """
        Closes the client.
        """
        if self.__channel is not None:
            self.__channel.close()
            # set to None so next time this client is used, it is reset
            self.__channel = None

    def __enter__(self):
        self.__get_channel()
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.close()
        # this check is needed in order to propagate errors
        return exception_type is None

    def __get_channel(self) -> grpc.Channel:
        """
        Instanciates and returns the channel.
        """
        if self.__channel is None:
            self.__channel = grpc.insecure_channel(target=self.config.endpoint)
        return self.__channel

    async def _run(
        self,
        *,
        with_stub: object,
        stub_func_name: str,
        initial_request: object,
        response_handler: TwoWayStreamResponseHandler,
    ) -> list[StreamResponse]:
        # TODO: (joey) throw clear errors here for auth/connection issues
        # TODO: (joey) implement some reconnect logic
        stub = with_stub(channel=self.__get_channel())
        stub_function = getattr(stub, stub_func_name)

        stream_responses = []
        q = queue.Queue()

        q.put(initial_request)

        def get_requests():
            while True:
                yield q.get()

        try:
            responses = stub_function(get_requests())

            for response in responses:
                next_request, two_way_response = response_handler(response)
                if two_way_response is not None:
                    stream_responses.append(two_way_response.stream)
                if next_request is not None:
                    q.put(next_request)
        except Exception as e:
            print("ERROR WHILE GETTING RESPONSES", e)
            raise e

        return stream_responses


__pdoc__ = {"StreamResponse": False}
