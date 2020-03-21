#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 21:59
# @Author  : lzm
# @File    : read_data.py

import pymysql
import time
import csv
from baidu_trans.my_config.application_parameter import params
from baidu_trans.trans.trans_word import trans_keyword as tk
from baidu_trans.trans.tencent_tarns import tencent as te

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
    trans_list = []
    connect = get_connect()
    try:
        cursor = connect.cursor()
        sql = 'select * from {table}  limit 0, 5 '.format(table=table)
        cursor.execute(sql)
        results = cursor.fetchall()
        print('查询到的数据条数>>>[%s]' % cursor.rowcount)
        for data in results:
            direct = {'src': data[1], 'baidu_trans': tk(data[1]), 'tencent_trans': te(data[1])}
            trans_list.append(direct)
            time.sleep(2)
    except Exception as e:
        print('查询数据时出现异常,异常原因：%s' % e)
    finally:
        close_connect(connect)
    return trans_list


def export_csv(data):
    """
    将翻译后的数据导出到csv文件中
    :return:
    """
    with open('f:/data.csv', 'a', encoding='utf-8-sig') as file:
        # writer = csv.writer(file, delimiter=' ')
        fieldnames = ['src', 'baidu_trans', 'tencent_trans']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    export_csv(get_data())


