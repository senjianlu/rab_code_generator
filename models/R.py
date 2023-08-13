#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rabbir/rab_code_generator/R.py
# @DATE: 2023/08/13 周日
# @TIME: 21:13:24
#
# @DESCRIPTION: R 结果类


class R(object):

    # 状态码
    code = None
    # 消息
    msg = None
    # 数据
    data = None
    # 分页
    total = None

    def __init__(self, code, msg, data=None, total=None):
        """
        @description: 初始化
        @param {type} 
        code: 状态码
        msg: 消息
        data: 数据
        total: 分页
        @return: 
        """
        self.code = code
        self.msg = msg
        self.data = data
        self.total = total
