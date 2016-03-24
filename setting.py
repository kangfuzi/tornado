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
    define('mongo_ip', default='127.0.0.1:27017')
    define('mongo_db', default='')
    define('mysql_user', default='')
    define('mysql_password', default='')
    define('mysql_host', default='')
    define('mysql_db_name', default='')
