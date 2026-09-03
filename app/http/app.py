#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/8/19 21:49
@Author: hallieliu123@163.com
@File  : app.py
"""
import dotenv
from flask_migrate import Migrate
from injector import Injector

from config import Config
from internal.extension import ExtensionModule
from internal.router import Router
from internal.server import Http
from pkg.custom_sqlalchemy import SQLAlchemy

# add .env to the project
dotenv.load_dotenv()

config = Config()
injector = Injector([ExtensionModule])
app = Http(
    __name__,
    migrate=injector.get(Migrate),
    db=injector.get(SQLAlchemy),
    config=config,
    router=injector.get(Router)
)

if __name__ == '__main__':
    app.run(debug=True)
