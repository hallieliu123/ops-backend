#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/8/29 13:46
@Author: hallieliu123@163.com
@File  : app_schema.py
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class CompletionRequest(FlaskForm):
    # validate endpoint chat/completion
    query = StringField('query', validators=[
        DataRequired(message="输入不能为空哦..."),
        Length(max=2000, message="输入最长不能超过2000个字符哦.")
    ])
