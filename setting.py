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
