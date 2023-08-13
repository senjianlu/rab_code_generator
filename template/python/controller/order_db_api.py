#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rabbir/rab_code_generator/template/python/controller/order_db_api.py
# @DATE: 2023/08/13 周日
# @TIME: 20:49:45
#
# @DESCRIPTION: 订单数据库操作 API 接口


import json
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, Text
from fastapi import APIRouter, Depends, Request, HTTPException


ROUTER = APIRouter(
    prefix=["/order_db_api"],
    tags=["auto_generate"],
)


class Order(BaseModel):
    """
    @description: 订单表
    """

    # 表名
    # __tablename__ = "order"
    # 表结构
    id: String
    order_id: String
    order_type: Integer
    order_status: Integer
    order_amount: Float
    order_time: DateTime
    order_remark: Text
    is_deleted: Boolean
    create_time: DateTime
    update_time: DateTime



@ROUTER.get("/list")
async def list(request: Request, order_for_list: Order):
    """
    @description: 订单列表
    """
    session = request.state.session
    # 1. 查询订单列表（排除空值）
    result = session.query(Order).filter(
        **order_for_list.dict(exclude_unset=True)
    ).all()
    # 2. 返回结果
    return {
        "code": 200,
        "msg": "success",
        "data": {
            "list": result,
            "total": len(result),
            "page": 1   
        }
    }