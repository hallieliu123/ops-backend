#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/8/29 14:01
@Author: hallieliu123@163.com
@File  : app_config.py
"""
import os

from .default_config import DEFAULT_CONFIG


def _get_env(key: str):
    return os.getenv(key, DEFAULT_CONFIG.get(key))


def _get_bool_env(key: str):
    val = _get_env(key)
    return val.lower() == "true" if val is not None else False


class Config:
    def __init__(self):
        # wtf csrf config
        self.WTF_CSRF_ENABLED = _get_env("WTF_CSRF_ENABLED")

        # sqlalchemy config imported
        self.SQLALCHEMY_DATABASE_URI = _get_env("SQLALCHEMY_DATABASE_URI")
        self.SQLALCHEMY_TRACK_MODIFICATION = _get_bool_env("SQLALCHEMY_TRACK_MODIFICATION")
        self.SQLALCHEMY_ECHO = _get_bool_env("SQLALCHEMY_ECHO")
        self.SQLALCHEMY_ENGINE_OPTIONS = {
            "pool_size": int(_get_env("SQLALCHEMY_POOL_SIZE")),
            "pool_recycle": int(_get_env("SQLALCHEMY_POOL_RECYCLE")),
        }
