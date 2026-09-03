#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/9/1 20:00
@Author: hallieliu123@163.com
@File  : app.py
"""
import uuid
from datetime import datetime

from sqlalchemy import (
    PrimaryKeyConstraint,
    Index,
    Column,
    UUID,
    Text,  # text
    String,  # varchar
    DateTime,  # timestamp
)
from sqlalchemy.dialects.postgresql import JSONB

from internal.extension import db


class App(db.Model):
    __tablename__ = "app"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="pk_app_id"),
        Index("idx_app_account_id", "account_id")
    )
    id = Column(UUID, default=uuid.uuid4, nullable=False)
    account_id = Column(UUID, default="", nullable=False)
    status = Column(String(255), default="", nullable=False)
    name = Column(String(255), default="", nullable=False)
    icon = Column(String(255), default="", nullable=False)
    description = Column(Text, default="", nullable=False)
    config = Column(JSONB, default={}, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
