#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/8/19 21:21
@Author: hallieliu123@163.com
@File  : router.py
"""
from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject
@dataclass
class Router:
    appHandler: AppHandler

    def register_routes(self, app: Flask):
        # 1.创建蓝图
        bp = Blueprint('ops-api', __name__, url_prefix='')
        # 2.将访问的url与handler控制器连接
        bp.add_url_rule('/ping', view_func=self.appHandler.ping)

        bp.add_url_rule('/apps/<uuid:app_id>/debug', methods=["POST"], view_func=self.appHandler.debug)

        bp.add_url_rule('/app', methods=["POST"], view_func=self.appHandler.create_app)
        bp.add_url_rule('/app/<uuid:app_id>', methods=["POST"], view_func=self.appHandler.get_app)
        bp.add_url_rule('/app/<uuid:app_id>/update', methods=["POST"], view_func=self.appHandler.update_app)
        bp.add_url_rule('/app/<uuid:app_id>/delete', methods=["POST"], view_func=self.appHandler.delete_app)
        # 3.应用上注册蓝图
        app.register_blueprint(bp)
