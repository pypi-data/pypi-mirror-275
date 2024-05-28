"""
kanstream
=====
kanstream is a media streaming library that provides the ability to create stream receivers and stream senders.

Example usage
---------

1. Create a new stream receiver and sender by `KanStream.create_stream`

```python
from kanstream import KanStream, StreamType

# create a new stream receiver
receiver = KanStream.create_stream("127.0.0.1", 8080, "my_client_id", stream_type=StreamType.RECEIVER)
for frame in receiver.receive():
    # process the frame

# create a new stream sender
sender = KanStream.create_stream("127.0.0.1", 8080, "my_client_id", stream_type=StreamType.SENDER)
sender.send(frame)
```

2. Create a new stream receiver and sender by `KanStream.create_receiver` and `KanStream.create_sender`

```python
from kanstream import KanStream, StreamType

# create a new stream receiver
receiver = KanStream.create_receiver("127.0.0.1", 8080, "my_client_id", codec_type=CodecType.H264)
for frame in receiver.receive():
    # process the frame


# create a new stream sender
sender = KanStream.create_sender("127.0.0.1", 8080, "my_client_id", codec_type=CodecType.H264)
sender.send(frame)

``` 
"""


__all__ = "KanStream", "StreamType", "StreamReceiver", "StreamSender", "CodecType"

from enum import Enum

from .stream.receiver import StreamReceiver
from .stream.sender import StreamSender
from .codec import CodecType


class StreamType(Enum):
    """
    The type of the stream.

    Attributes:
        RECEIVER: The stream is a receiver.
        SENDER: The stream is a sender.
    """

    RECEIVER = 1
    SENDER = 2


class KanStream:

    streams = {
        StreamType.RECEIVER: StreamReceiver,
        StreamType.SENDER: StreamSender
    }

    @classmethod
    def create_stream(
        cls, host: str, port: int, client_id: str,
        *, codec_type=CodecType.H264, stream_type: StreamType
    ) -> StreamReceiver | StreamSender:
        """
        Create a new stream object based on the given stream type.

        Args:
            host (str): The host address of the server.
            port (int): The port number of the server.
            client_id (str): The client ID of the stream.
            codec_type (CodecType): The codec type of the stream.
            stream_type (StreamType): The type of the stream.
        Returns:
            A stream object.
        """

        if stream_type not in cls.streams:
            raise ValueError(f"Invalid stream type: {stream_type}")
        return cls.streams[stream_type](host, port, client_id, codec_type=codec_type)

    @staticmethod
    def create_receiver(host, port, client_id, *, codec_type=CodecType.H264):
        """
        create a new receiver stream object.

        Args:
            host (str): server host address.
            port (int): server port number.
            client_id (str): stream client ID.
            codec_type (CodecType): stream codec type.
        Returns:
            a receiver stream object.
        """
        return StreamReceiver(host, port, client_id, codec_type=codec_type)

    @staticmethod
    def create_sender(host, port, client_id, codec_type=CodecType.H264):
        """
        create a new sender stream object.

        Args:
            host (str): server host address.
            port (int): server port number.
            client_id (str): stream client ID.
            codec_type (CodecType): stream codec type.
        Returns:
            a sender stream object.
        """
        return StreamSender(host, port, client_id, codec_type=codec_type)
