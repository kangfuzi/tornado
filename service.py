# coding=utf-8
import tornado.ioloop
import tornado.web
import os
import signal
from tornado.options import options
import logging

from setting import define_options


from jinja2 import ChoiceLoader, FileSystemLoader
from template import JinjaLoader
from common import common

from handlers.base_handler import BaseHandler
from handlers.main_handler import MainHandler
from handlers.login_handler import LoginHandler

define_options()
options.parse_command_line()

common.set_log()

loader = ChoiceLoader([
    FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
 ])

settings = {
        "template_loader": JinjaLoader(loader=loader, auto_escape=False),
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "debug": options.debug,
        "gzip": True,
        "cookie_secret": "35oETzKXQAGaYdkL6gEmGeJJFuYh7EQnp3XdTP1o/Vo=",
        "log_function": common.web_log,
        "login_url": "/login/"
        }

routs = [
    (r"/?", BaseHandler),
    (r"/main/([a-zA-Z]*)/?", MainHandler),
    (r"/login/([a-zA-Z]*)/?", LoginHandler),
]

application = tornado.web.Application(routs, **settings)


def sigint_handler():
    tornado.ioloop.IOLoop.instance().stop()


if __name__ == "__main__":
    logging.info('service start!')
    # logging.info('Current host: %s' %(options.mongo_ip))
    # logging.info('Current db_name: %s' %(options.mongo_db))
    application.listen(options.port)
    signal.signal(signal.SIGTERM, sigint_handler)
    signal.signal(signal.SIGINT, sigint_handler)
    tornado.ioloop.IOLoop.instance().start()
