import json


def decode_body_and_convert_to_dict(body: bytes):
    return json.loads(body.decode('utf-8'))
