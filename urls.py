# coding: utf-8

import tornado.web

from settings import settings
from views import MainHandler

application = tornado.web.Application([
    (r"^/", MainHandler),

], **settings)