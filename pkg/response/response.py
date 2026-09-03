#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/8/29 15:08
@Author: hallieliu123@163.com
@File  : response.py
"""
from dataclasses import dataclass, field
from typing import Any

from flask import jsonify

from .http_code import HttpCode


@dataclass
class Response:
    code: str = HttpCode.SUCCESS
    message: str = ""
    data: Any = field(default_factory=dict)


def json(data: Response = None):
    return jsonify(data), 200


def success_json(data: Any = None):
    return json(Response(code=HttpCode.SUCCESS, message="", data=data))


def fail_json(data: Any = None):
    return json(Response(code=HttpCode.FAILED, message="", data=data))


def validate_error_json(errors: dict):
    first_key = next(iter(errors))
    if first_key is not None:
        msg = errors.get(first_key, [])[0]
    else:
        msg = ""

    return json(Response(code=HttpCode.VALIDATION_ERROR, message=msg, data=errors))


def message(code: str, msg: str = ""):
    return jsonify(Response(code=code, message=msg, data={})), 200


def success_message(msg: str = ""):
    return message(code=HttpCode.SUCCESS, msg=msg)


def fail_message(msg: str = ""):
    return message(code=HttpCode.FAILED, msg=msg)


def unauthorized_message(msg: str = ""):  # 401
    return message(code=HttpCode.UNAUTHORIZED, msg=msg)


def forbidden_message(msg: str = ""):  # 403
    return message(code=HttpCode.FORBIDDEN, msg=msg)


def not_found_message(msg: str = ""):  # 404
    return message(code=HttpCode.NOT_FOUND, msg=msg)


def method_not_allowed_message(msg: str = ""):  # 405
    return message(code=HttpCode.METHOD_NOT_ALLOWED, msg=msg)
