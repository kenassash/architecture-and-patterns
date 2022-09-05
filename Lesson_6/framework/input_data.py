import quopri


class ParseInputData:

    @staticmethod
    def parser_data(data: str):

        query_param = {}
        if data:
            params = data.split('&')
            for item in params:
                k, v = item.split('=')
                query_param[k] = v
        return query_param


class DecoderInputData:

    @staticmethod
    def decode_value(data):
        decoding_data = {}
        for k, v in data.items():
            # print(v)
            value = bytes(v.replace('%', '=').replace('+', ' '), 'UTF-8')
            # print(value)
            decode_string = quopri.decodestring(value).decode('UTF-8')
            decoding_data[k] = decode_string
        return decoding_data
