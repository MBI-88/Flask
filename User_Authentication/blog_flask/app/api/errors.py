# API errors
# Packages

from flask import jsonify
from app.exceptions import ValidationError
from . import api

# Functions

def bad_request(message) -> jsonify:
    response = jsonify({'error': 'bad request', 'message': message})
    response.status_code = 400
    return response


def unauthorized(message) -> jsonify:
    response = jsonify({'error': 'unauthorized', 'message': message})
    response.status_code = 401
    return response


def forbidden(message) -> jsonify:
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


@api.errorhandler(ValidationError)
def validation_error(e) -> ValidationError:
    return bad_request(e.args[0])