#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/8/19 21:42
@Author: hallieliu123@163.com
@File  : http.py
"""
import os

from flask import Flask
from flask_migrate import Migrate

from config import Config
from internal.exception import CustomException
from internal.router import Router
from pkg.custom_sqlalchemy import SQLAlchemy
from pkg.response import Response, json, HttpCode


class Http(Flask):
    def __init__(self, *args, migrate: Migrate, db: SQLAlchemy, config: Config, router: Router, **kwargs):
        # 1.初始化父类函数
        super().__init__(*args, **kwargs)

        # config inject
        self.config.from_object(config)  # 配置注入

        # 2.注册应用路由
        router.register_routes(self)

        self.register_error_handler(Exception, self._register_error_handler)  # 异常捕获

        # 初始化flask扩展
        db.init_app(self)
        migrate.init_app(self, db, directory="internal/migrations")

    def _register_error_handler(self, error: Exception):
        if isinstance(error, CustomException):
            return json(Response(
                code=error.code,
                message=error.message,
                data=error.data if error.data is not None else {},
            ))
        if self.debug or os.getenv("FLASK_DEBUG") == "development":
            raise error
        else:
            return json(Response(
                code=HttpCode.FAILED,
                message=str(error),
                data={})
            )
