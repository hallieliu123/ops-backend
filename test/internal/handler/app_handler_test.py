#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/9/1 11:06
@Author: hallieliu123@163.com
@File  : app_handler_test.py.py
"""
import pytest

from pkg.response import HttpCode


class TestAppHandler:
    @pytest.mark.parametrize('query', [None, 'who are you ?'])
    def test_completion(self, query, client):
        res = client.post('/chat/completions', json={'query': query})
        assert res.status_code == 200
        if query is None:
            assert res.json.get('code') == HttpCode.VALIDATION_ERROR
        else:
            assert res.json.get('code') == HttpCode.SUCCESS
