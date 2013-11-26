import json

from flask import make_response


def json_response(data, status=200):
    response = make_response(json.dumps(data), status)
    response.mimetype = 'application/json'
    return response


def txt_response(data, status=200):
    response = make_response(data, status)
    response.mimetype = 'text/plain'
    return response
