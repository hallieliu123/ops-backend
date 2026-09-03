#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/9/2 15:27
@Author: hallieliu123@163.com
@File  : sqlalchemy.py.py
"""

from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy


class SQLAlchemy(_SQLAlchemy):

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
