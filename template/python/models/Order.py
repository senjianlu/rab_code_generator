#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rabbir/rab_code_generator/template/python/models/Order.py
# @DATE: 2023/08/13 周日
# @TIME: 20:56:48
#
# @DESCRIPTION: 订单表


from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Order(Base):
    """
    @description: 订单表
    """

    # 表名
    __tablename__ = "order"
    # 表结构
    id = Column(Integer, primary_key=True, autoincrement=True, comment="主键")
    order_id = Column(String(32), nullable=False, comment="订单号")
    order_type = Column(Integer, nullable=False, comment="订单类型")
    order_status = Column(Integer, nullable=False, comment="订单状态")
    order_amount = Column(Float, nullable=False, comment="订单金额")
    order_time = Column(DateTime, nullable=False, comment="订单时间")
    order_remark = Column(Text, nullable=True, comment="订单备注")
    is_deleted = Column(Boolean, nullable=False, default=False, comment="是否删除")
    create_time = Column(DateTime, nullable=False, comment="创建时间")
    update_time = Column(DateTime, nullable=False, comment="更新时间")
