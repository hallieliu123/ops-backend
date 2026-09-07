#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/8/19 21:11
@Author: hallieliu123@163.com
@File  : app_handler.py
"""
import uuid
from dataclasses import dataclass

import dotenv
from flask import request
from injector import inject
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
# from openai import OpenAI
from langchain_openai import ChatOpenAI

from internal.exception import FailedException
from internal.schema import CompletionRequest
from internal.service import AppService
from pkg.response import success_message, success_json, validate_error_json

dotenv.load_dotenv()


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

    def debug(self, app_id: uuid.UUID):
        # validate query
        req = CompletionRequest()
        if not req.validate():
            return validate_error_json(req.errors)

        prompt = ChatPromptTemplate.from_template("{query}")
        llm = ChatOpenAI(
            model="kimi-k2.6",
            temperature=1
        )
        parser = StrOutputParser()
        chain = prompt | llm | parser
        content = chain.invoke({"query": request.json.get("query")})

        return success_json({"content": content})

    def ping(self):
        raise FailedException("no data found...")
        # return {'ping': 'pong'}
