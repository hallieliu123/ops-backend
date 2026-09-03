#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/9/1 16:35
@Author: hallieliu123@163.com
@File  : default_config.py
"""
DEFAULT_CONFIG = {
    # sqlalchemy default config
    "SQLALCHEMY_DATABASE_URI": "postgresql://postgres:postgres@192.168.3.140:5432/llmops?client_encoding=utf8",
    "SQLALCHEMY_POOL_SIZE": "30",
    "SQLALCHEMY_POOL_RECYCLE": "3600",
    "SQLALCHEMY_RECORD_QUERIES": "False",
    "SQLALCHEMY_ECHO": "True",
    "SQLALCHEMY_TRACK_MODIFICATIONS": "False",

    # wtf csrf config
    "WTF_CSRF_ENABLED": "False"
}
