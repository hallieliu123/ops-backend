#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/9/1 16:27
@Author: hallieliu123@163.com
@File  : module_extension.py
"""
from flask_migrate import Migrate
from injector import Module, Binder

from pkg.custom_sqlalchemy import SQLAlchemy
from .data_extension import db
from .migrate_extension import migrate


class ExtensionModule(Module):
    def configure(self, binder: Binder):
        binder.bind(SQLAlchemy, to=db)
        binder.bind(Migrate, to=migrate)
