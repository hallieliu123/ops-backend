#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/8/29 17:35
@Author: hallieliu123@163.com
@File  : exception.py
"""
from dataclasses import field
from typing import Any

from pkg.response import HttpCode


class CustomException(Exception):
    code: str = HttpCode.FAILED
    message: str = ""
    data: Any = field(default_factory=dict)

    def __init__(self, message: str = "", data: Any = None):
        super().__init__()
        self.data = data
        self.message = message


class FailedException(CustomException):
    pass


class NotFoundException(CustomException):
    code: str = HttpCode.NOT_FOUND


class UnauthorizedException(CustomException):
    code: str = HttpCode.UNAUTHORIZED


class ForbiddenException(CustomException):
    code: str = HttpCode.FORBIDDEN


class ValidationErrorException(CustomException):
    code: str = HttpCode.VALIDATION_ERROR


class MethodNotAllowedException(CustomException):
    code: str = HttpCode.METHOD_NOT_ALLOWED
