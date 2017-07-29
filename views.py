# coding: utf-8

import tornado.web
import os
from settings import BASE_DIR

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("upload.html")


class CheckFileHandler(tornado.web.RequestHandler):

    def post(self):
        md5value = self.get_argument("md5value")
        filename = self.get_argument("filename")
        path_part = os.path.join(BASE_DIR, "file_upload/static/upload/" + md5value + ".part")
        path_ok = os.path.join(BASE_DIR, "file_upload/static/upload/" + md5value + ".ok")

        if os.path.isfile(path_ok):  # 文件上传结束
            flag = 2
            ret = {"flag": flag}
        elif os.path.isfile(path_part):
            flag = 1
            ret = {"flag": flag, "startindex": 1}
        else:
            flag = 0
            ret = {"flag": flag, "startindex": 0}

        self.write(ret)


class UploadJobHandler(tornado.web.RequestHandler):

    def post(self):
        file_metas = self.request.files["file"]
        if len(file_metas) <= 0:
            self.write("获取服务器上传文件失败！")

        metas = file_metas[0]
        md5value = self.get_argument("md5value")
        tempfilename = md5value + ".part"
        newname = os.path.join(BASE_DIR, "file_upload/static/upload/" + tempfilename)

        with open(newname, "ab") as f:  # 以二机制方式追加
            f.write(metas["body"])
        self.write("finished!")

    def get(self, *args, **kwargs):
        self.write("ok")


class FinishUpload(tornado.web.RequestHandler):

    def post(self, *args, **kwargs):
        md5value = self.get_argument("md5value")
        filename = self.get_argument("filename")
        totalsize = self.get_argument("totalsize")
        print totalsize

        path_part = os.path.join(BASE_DIR, "file_upload/static/upload/" + md5value + ".part")
        path_ok = os.path.join(BASE_DIR, "file_upload/static/upload/" + md5value + ".ok")
        old_name = os.path.join(BASE_DIR, "file_upload/static/upload/" + filename)

        with open(path_ok, "w") as f:
            print "创建ok文件"
        os.rename(path_part, old_name)
        self.write("{'data': 'ok'}")


