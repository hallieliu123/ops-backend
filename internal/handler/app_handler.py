#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/8/19 21:11
@Author: hallieliu123@163.com
@File  : app_handler.py
"""
import os
import uuid
from dataclasses import dataclass
from typing import cast, Any

from flask import request
from injector import inject
from openai import OpenAI

from internal.exception import FailedException
from internal.schema import CompletionRequest
from internal.service import AppService
from pkg.response import success_message, success_json, validate_error_json


@inject
@dataclass
class AppHandler:
    app_service: AppService

    def create_app(self):
        app = self.app_service.create_app()
        return success_message(msg=f"数据已经成功创建{app.id}")

    def get_app(self, app_id: uuid.UUID):
        app = self.app_service.get_app(app_id)
        return success_message(msg=f"数据已获取，我是{app.name}")

    def update_app(self, app_id: uuid.UUID):
        app = self.app_service.update_app(app_id)
        return success_message(msg=f"数据已更新{app.name}")

    def delete_app(self, app_id: uuid.UUID):
        app = self.app_service.delete_app(app_id)
        return success_message(msg=f"数据已删除{app.id}")

    def completion(self):
        # 1get query string post ? get ?
        query = request.json.get('query')

        # validate query
        req = CompletionRequest()
        if not req.validate():
            return validate_error_json(req.errors)
        # 1.create openAI client and send request
        client = OpenAI(
            api_key=os.getenv("MOONSHOT_API_KEY"),
            base_url=os.getenv('MOONSHOT_API_BASE')
        )
        mgs = [
            {"role": "system", "content": "你是一个聊天机器人，根据用户的提问回答问题。"},
            {"role": "user", "content": str(query)}
        ]
        completion = client.chat.completions.create(
            model="kimi-k2.6",
            messages=cast(Any, mgs)
        )
        # 2.return response to FE
        return success_json({"content": completion.choices[0].message.content})
        # return jsonify({"content": completion.choices[0].message.content}), 200

    def ping(self):
        raise FailedException("no data found...")
        # return {'ping': 'pong'}
