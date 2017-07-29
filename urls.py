# coding: utf-8

import tornado.web

from settings import settings
from views import MainHandler, UploadJobHandler, CheckFileHandler

application = tornado.web.Application([
    (r'^/', MainHandler),
    (r'^/uploadfile$', UploadJobHandler),
    (r'^/checkfile$', CheckFileHandler),

], **settings)