#!/usr/bin/env python
# -*- coding:utf8 -*-
# vim: set ts=4 sw=4 sts=4 tw=100 noet:

import logging 
from tornado.options import options
import logging.handlers
from tornado.log import access_log
from tornado.log import LogFormatter


def set_log():

    if options.log_path:
        nor = logging.getLogger('tornado.access')
        nor.setLevel(logging.INFO)
        filehandler = logging.handlers.TimedRotatingFileHandler(options.log_path, 'midnight', 1, 0)
        filehandler.suffix = "%Y%m%d.log"
        filehandler.setFormatter(LogFormatter())
        nor.addHandler(filehandler)


def web_log(handler):
    from handlers.base_handler import BaseHandler
    if isinstance(handler, BaseHandler):    # Avoid resource handle and static handler to call this handler
        if handler.get_status() < 400:
            log_method = access_log.info
        elif handler.get_status() < 500:
            log_method = access_log.warning
        else:
            log_method = access_log.error

        refer = handler.request.headers.get('Referer', '')
        request_time = 1000.0 * handler.request.request_time()
        log_method("%d ReferBala: %s %s %.2fms", handler.get_status(), refer, request_time)
        current_uid = 0
        log_method("ACCESS: %d\t%s\t%s\t%s\t%s\t%.2fms", handler.get_status(), handler.request.method,
                   handler.request.uri, handler.get_current_ip(), current_uid, request_time)
