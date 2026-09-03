#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/9/1 20:37
@Author: hallieliu123@163.com
@File  : app.py
"""
import uuid
from dataclasses import dataclass

from injector import inject

from internal.model import App
from pkg.custom_sqlalchemy import SQLAlchemy


@inject
@dataclass
class AppService:
    db: SQLAlchemy

    def create_app(self):
        with self.db.auto_commit():
            app = App(name="robot test", account_id=uuid.uuid4(), icon="", description="I'm a robot")
            self.db.session.add(app)
        return app

    def get_app(self, app_id: uuid.UUID):
        app = self.db.session.query(App).get(app_id)
        return app

    def update_app(self, app_id: uuid.UUID):
        with self.db.auto_commit():
            app = self.get_app(app_id)
            app.name = "Tesla Robot"
        return app

    def delete_app(self, app_id: uuid.UUID):
        with self.db.auto_commit():
            app = self.get_app(app_id)
            self.db.session.delete(app)
        return app
