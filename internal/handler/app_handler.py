#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/8/19 21:11
@Author: hallieliu123@163.com
@File  : app_handler.py
"""
import uuid
from dataclasses import dataclass
from operator import itemgetter

import dotenv
from flask import request
from injector import inject
from langchain.memory import ConversationBufferWindowMemory
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.memory import BaseMemory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableConfig
from langchain_core.tracers import Run
# from openai import OpenAI
from langchain_openai import ChatOpenAI

from internal.exception import FailedException
from internal.schema import CompletionRequest
from internal.service import AppService, VectorDBService
from pkg.response import success_message, success_json, validate_error_json

dotenv.load_dotenv()


@inject
@dataclass
class AppHandler:
    app_service: AppService
    vector_service: VectorDBService

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

        prompt = ChatPromptTemplate.from_messages([
            ("system",
             "你是无所不知的聊天机器人，上下文里存放的是人类与你对话的信息列表。根据用户的提问和参照文本<context>{context}</context>回答用户的问题。"),
            MessagesPlaceholder("history"),
            ("human", "{query}"),
        ])

        llm = ChatOpenAI(
            model="kimi-k2.6",
            temperature=1
        )
        memory = ConversationBufferWindowMemory(
            k=6,
            input_key="query",
            return_messages=True,
            memory_key="history",
            chat_memory=FileChatMessageHistory("../../storage/history.txt")
        )
        retriever = self.vector_service.get_retriever() | self.vector_service.combine_documents
        chain = (RunnablePassthrough.assign(
            history=RunnableLambda(memory.load_memory_variables) | itemgetter("history"),
            context=itemgetter("query") | retriever
        ) | prompt | llm | StrOutputParser()).with_listeners(on_end=self._save_context)
        chain_input = {"query": request.json.get("query")}
        content = chain.invoke(chain_input, config={"configurable": {"memory": memory}})

        print("history: ", memory.load_memory_variables({}))

        return success_json({"content": content})

    def _save_context(self, run_obj: Run, config: RunnableConfig):
        configurable = config.get("configurable", {})
        memory = configurable.get("memory", None)
        print("config: ", config)
        print("run_obj.outputs: ", run_obj.outputs)
        print("run_obj.inputs: ", run_obj.inputs)
        if memory is not None and isinstance(memory, BaseMemory):
            memory.save_context(run_obj.inputs, run_obj.outputs)

    def ping(self):
        raise FailedException("no data found...")
        # return {'ping': 'pong'}
