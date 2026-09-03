#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/8/29 15:08
@Author: hallieliu123@163.com
@File  : http_code.py
"""
from enum import Enum


class HttpCode(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"
    FORBIDDEN = "forbidden"
    NOT_FOUND = "not_found"
    UNAUTHORIZED = "unauthorized"
    VALIDATION_ERROR = "validation_error"
    METHOD_NOT_ALLOWED = "method_not_allowed"
