# coding: utf-8
import tornado.ioloop
import os
import sys

from tornado.options import options, parse_command_line
from urls import application

reload(sys)
sys.setdefaultencoding('utf8')

basePath = os.path.dirname(os.path.dirname(__file__))


if __name__ == "__main__":
    parse_command_line()
    application.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
