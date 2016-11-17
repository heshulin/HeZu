# -*- coding:utf-8 -*
from HeZe.bean.qiniuup import up
from HeZe.bean.usetphotorandom import getuserphotorandom
from PIL import Image

ALLOWED_TYPE = ['png', 'jpeg', 'jpg']


class upimage(object):

    def allowed_file(self, filetype):
        return filetype in ALLOWED_TYPE

    def upuserphoto(self, file, Space):
        try:
            img = Image.open(file)
            type = 'jpg'
            if file and self.allowed_file(type):
                # 图片名字
                #img.thumbnail((500, 500), Image.ANTIALIAS)  # 对图片进行等比缩放
                filename = getuserphotorandom() + '.png'
                path = 'C:/images/' + filename
                print(path)
                img.save(path, "png")  # 保存图片
                url = up(path, Space)
                state = 1
                msg = '上传成功'
            else:
                msg = "请合法上传！"
                state = 0
                url = ''
        except Exception as e:
            state = 0
            msg = "出现未知的错误了哦~，再试试吧"
            url = ''
        array = {
            'state': state,
            'msg': msg,
            'url': url
        }
        return array