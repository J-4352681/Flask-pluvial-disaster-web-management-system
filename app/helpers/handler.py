from flask import render_template, request
from flask.json import jsonify


def unauthorized_error(e):
    kwargs = {
        "error_name": "401 Unauthorized Error",
        "error_description": "No está autenticado para acceder a la url",
    }
    return make_response(kwargs, 401)


def forbidden_error(e):
    kwargs = {
        "error_name": "403 Forbidden Error",
        "error_description": "No está autorizado para acceder a la url",
    }
    return make_response(kwargs, 403)


def not_found_error(e):
    kwargs = {
        "error_name": "404 Not Found Error",
        "error_description": "La url a la que quiere acceder no existe",
    }
    return make_response(kwargs, 404)


def internal_server_error(e):
    kwargs = {
        "error_name": "500 Internal Server Error",
        "error_description": "Se produjo un error en el servidor",
    }
    return make_response(kwargs, 505)


def make_response(data, status):
    if request.path.startswith("/api/"):
        return jsonify(data), status
    else:
        return render_template("error.html", **data), status