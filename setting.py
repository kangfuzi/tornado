#!/usr/bin/env python
# -*- coding:utf8 -*-
# vim: set ts=4 sw=4 sts=4 tw=100 noet:

from tornado.options import define
import logging


def define_options():

    define('log_level', default=logging.INFO)
    define('debug', default=1)
    define('port', default=8999)
    define('log_path')
    define('mongo_ip',default='127.0.0.1:27017')
    define('mongo_db', default = 'dms')
    define('mysql_user', default='root')
    define('mysql_password', default='ABCabc123')
    define('mysql_host', default='123.56.146.31')
    define('mysql_db_name', default='yingyangshi')
