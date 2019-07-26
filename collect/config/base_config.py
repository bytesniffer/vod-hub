#!/usr/bin/ python
# -*- coding: utf-8 -*-
__author__ = 'bytesniffer'
__date__ = '2019-7-25 23:59'


SQL_URL = '127.0.0.1'
SQL_USER = 'root'
SQL_PASSWORD = '123456'
DATABASE = 'movie'
ADMIN = 'waert'
ADMIN_PASSWORD = '123456'

SQLALCHEMY_DATABASE_URI = """mysql+pymysql://{SQL_USER}:{SQL_PASSWORD}@{SQL_URL}:3306/{DATABASE}""".format(
                          SQL_USER=SQL_USER,
                          SQL_PASSWORD=SQL_PASSWORD,
                          SQL_URL=SQL_URL,
                          DATABASE=DATABASE)
