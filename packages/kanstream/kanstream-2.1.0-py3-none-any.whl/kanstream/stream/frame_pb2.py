from dataclasses import dataclass

import betterproto


@dataclass
class MessageBody(betterproto.Message):
    
    client_id: str = betterproto.string_field(1)

    message: str = betterproto.string_field(2)

    codec_type: int = betterproto.int32_field(3)

    width: int = betterproto.int32_field(4)

    height: int = betterproto.int32_field(5)

    frames_per_second: int = betterproto.int32_field(6)

    frame_type: int = betterproto.int32_field(7)

    rotation: int = betterproto.int32_field(8)

    track_id: int = betterproto.int32_field(9)

    capture_time_ms: int = betterproto.int64_field(10)

    render_time_ms: int = betterproto.int64_field(11)

    internal_send_ts: int = betterproto.int64_field(12)

    uid: int = betterproto.int32_field(13)

    stream_type: int = betterproto.int32_field(14)

    image_buffer: bytes = betterproto.bytes_field(15)

    length: int = betterproto.int64_field(16)

    message_type: int = betterproto.int32_field(17)
