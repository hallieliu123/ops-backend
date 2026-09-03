#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/8/19 17:20
@Author: hallieliu123@163.com
@File  : __init__.py.py
"""
from .exception import (
    CustomException,
    FailedException,
    ForbiddenException,  # 403
    NotFoundException,  # 404
    MethodNotAllowedException,  # 405
    UnauthorizedException,  # 401
    ValidationErrorException
)

__all__ = [
    "CustomException",
    "FailedException",
    "ForbiddenException",
    "NotFoundException",
    "MethodNotAllowedException",
    "UnauthorizedException",
    "ValidationErrorException",
]
