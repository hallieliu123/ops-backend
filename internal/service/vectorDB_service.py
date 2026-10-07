#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time  : 2026/10/6 14:46
@Author: hallieliu123@163.com
@File  : vectorDB_service.py
"""
import os

from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_postgres import PGVector


class VectorDBService:
    def __init__(self):
        embeddings = DashScopeEmbeddings(model="text-embedding-v2")
        vector_store = PGVector(
            embeddings=embeddings,
            connection=os.getenv("SQLALCHEMY_VECTOR_DATABSE_URI"),
            # collection_name=embeddings.model,
            collection_name="my_queen",
        )
        self.vector_store = vector_store

    def get_retriever(self) -> VectorStoreRetriever:
        return self.vector_store.as_retriever()

    @classmethod
    def combine_documents(cls, documents: list) -> str:
        return "\n".join([doc.page_content for doc in documents])
