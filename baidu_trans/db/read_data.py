#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 21:59
# @Author  : lzm
# @File    : read_data.py

import pymysql
import time
from baidu_trans.my_config.application_parameter import params
from baidu_trans.trans.trans_word import trans_keyword as tk

"""
从mysql中读取数据
"""
database = 'spiders'
table = 'spider'


def get_connect():
    """
    获取数据库链接
    :return:
    """
    host = str(params['platform']['mysql']['host'])
    port = params['platform']['mysql']['port']
    user = str(params['platform']['mysql']['user'])
    password = str(params['platform']['mysql']['password'])

    print('数据库信息：host=%s, port=%s, user=%s, password=%s, db=%s' % (host, port, user, password, database))

    connect = pymysql.connect(host=host, port=port, user=user, password=password, db=database)
    return connect


def close_connect(connect):
    """
    关闭数据库链接
    :param connect:
    :return:
    """
    connect.close()


def get_data():
    """
    从数据库中读取数据
    :return:
    """
    connect = get_connect()
    try:
        cursor = connect.cursor()
        sql = 'select * from {table} '.format(table=table)
        cursor.execute(sql)
        results = cursor.fetchall()
        print('查询到的数据条数>>>[%s]' % cursor.rowcount)
        # print('查询结果：%s' % results)
        # print(type(results))
        for data in results:
            print('原始关键词{src}，翻译后的关键词{dest}'.format(src=data[1], dest=tk(data[1])))
            time.sleep(2)
    except Exception as e:
        print('查询数据时出现异常,异常原因：%s' % e)
    finally:
        close_connect(connect)


get_data()
