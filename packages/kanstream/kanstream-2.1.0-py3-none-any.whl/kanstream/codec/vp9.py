import av
import av.video

from .abc import VideoDecodeABC
from .h264 import H264Encoder
from ..utils.calculate_bitrate import calculate_bitrate

class VP9Encoder(H264Encoder):
    
    def set_config(self, height: int, width: int, fps: int, gop_size=60, bit_rate=0):
        container: av.OutputContainer = av.open('output.webm', 'w')
        stream: av.video.stream.VideoStream = container.add_stream('vp9', rate=30)

        # 编码器相关配置
        bit_rate = bit_rate if bit_rate > 0 else calculate_bitrate(width, height, fps) * 2
        codec_context = stream.codec_context
        codec_context.bit_rate = bit_rate * 1000
        codec_context.bit_rate_tolerance = 200 * 1000
        codec_context.framerate = fps
        codec_context.gop_size = gop_size
        codec_context.pix_fmt = 'yuv420p'
        codec_context.options = {
            'preset': 'ultrafast',
        }
        stream.height = height
        stream.width = width

        self._stream = stream
        self._container = container

        return bit_rate


class VP9Decoder(VideoDecodeABC):
    pass
