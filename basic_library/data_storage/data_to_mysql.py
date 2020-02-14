#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 21:57
# @Author  : lzm
# @File    : data_to_mysql.py

import pymysql

'''
python3操作mysql，存储数据
'''

# mysql信息
host = '127.0.0.1'
port = 3306
user_name = 'root'
pass_word = 'root'




def create_table():
    db = pymysql.connect(host=host, user=user_name, password=pass_word, port=port)
    cursor = db.cursor()
    # cursor.execute('select version()')
    # data = cursor.fetchone()
    # print(data)

    cursor.execute('create database spiders default  character set utf8mb4')
    cursor.execute('use spiders')
    create_table_sql = 'create table if not exists movies(id varchar(10) not null, sort int(4) not null , movie_name varchar(50) not null ,star varchar(255) not null ,relase_time varchar(255) not null ,score varchar(255) not null,primary key  (id))'
    cursor.execute(create_table_sql)
    db.close()


def insert_data():

    db = pymysql.connect(host=host, user=user_name, password=pass_word, port=port)
    cursor = db.cursor()
    cursor.execute('use spiders')
    sql = 'insert into movies(id, movie_name, sort, star, relase_time, score)values (%s, %s, %s, %s, %s, %s)'
    try:
        cursor.execute(sql, ('1', 1, '1', '1', '1', '1'))
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()


def main():
    # create_table()
    insert_data()


main()
