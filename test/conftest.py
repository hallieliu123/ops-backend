#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/9/1 11:30
@Author: hallieliu123@163.com
@File  : conftest.py
"""

# 强行把当前项目的根目录塞进 Python 的搜索路径里


import pytest

from app.http import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
