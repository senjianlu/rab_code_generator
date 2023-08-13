#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rabbir/rab_code_generator/main.py
# @DATE: 2023/08/13 周日
# @TIME: 09:53:46
#
# @DESCRIPTION: 代码生成器主程序


from sqlalchemy.orm import Session
from sqlalchemy.sql import text


def main(table_name: str, session: Session):
    """
    @description: 主方法
    """
    # 0. 检查 SQL 连接，如果没有连接就退出
    if session is None:
        print("SQL 连接失败")
        return
    # 1. 读取表结构
    table = session.execute(text("SELECT * FROM information_schema.TABLES WHERE TABLE_NAME = '%s'" % table_name)).first()
    if table is None:
        print("表不存在")
        return
    # 读取表结构和表注释
    sql_str = f"""
            SELECT
            tb.table_name,
            d.objsubid,
            d.description,
            e.*
        FROM
            information_schema.tables tb
                JOIN pg_class c ON c.relname = tb.table_name
                LEFT JOIN pg_description d ON d.objoid = c.oid
                LEFT JOIN information_schema.COLUMNS e ON d.objsubid = e.ordinal_position
        WHERE
            tb.table_name = '{table_name}'
        and e.TABLE_NAME = '{table_name}'
        """
    table_columns = session.execute(text(sql_str)).fetchall()
    # for talbe_column in table_columns:
    #     print(talbe_column)
    # 2. 生成后端代码
    # 2.1 controller
    # 3. 生成前端代码
    # 3.1 typing.d.ts
    # 3.2 api.ts
    # 3.3 页面代码


if __name__ == "__main__":
    main("pp_node", None)