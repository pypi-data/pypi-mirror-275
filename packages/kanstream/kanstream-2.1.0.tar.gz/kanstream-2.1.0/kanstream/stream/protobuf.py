from google.protobuf.internal.encoder import _VarintBytes


class ProtobufVarint32LengthFieldEncoder(object):

    @staticmethod
    def encode(message_bytes: bytes):
        message_length = len(message_bytes)
        varint_encoded_length = _VarintBytes(message_length)
        encoded_message = varint_encoded_length + message_bytes

        return encoded_message


class ProtobufVarint32FrameDecoder(object):

    def __init__(self):
        self.buffer = b''

    def decode(self, data: bytes):
        self.buffer += data
        messages = []
        while True:

            if len(self.buffer) < 1:
                break

            message_length, consumed_bytes = self._read_varint32(self.buffer)

            if len(self.buffer) < consumed_bytes + message_length:
                break

            message_data = self.buffer[consumed_bytes:consumed_bytes + message_length]
            messages.append(message_data)
            self.buffer = self.buffer[consumed_bytes + message_length:]

        return messages

    @staticmethod
    def _read_varint32(data: bytes):

        value = 0
        shift = 0
        consumed_bytes = 0
        for i in range(len(data)):
            byte = data[i]
            value |= (byte & 0x7F) << shift
            consumed_bytes += 1

            if not byte & 0x80:
                break

            shift += 7

        return value, consumed_bytes
