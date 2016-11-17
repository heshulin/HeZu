# -*- coding:utf-8 -*-
from qiniu import Auth, put_file, etag
from HeZe.bean.usetphotorandom import getuserphotorandom


def up(imagelocation,bucketname):
    q = Auth("gFO-8IYwjVPzNAmbAORHJCgGwIHzcyIbFhZ3yVIi", "hllClWcBETkcn0aI8SROEe4Y1blV5gEQwgUHAQQu")
    bucket_name = bucketname
    #图片名字
    key = getuserphotorandom()
    token = q.upload_token(bucket_name, key)
    localfile = imagelocation
    ret, info = put_file(token, key, localfile)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)
    if bucketname == "hezu":
        return "http://ogaw9rqk7.bkt.clouddn.com/" + key + "?imageView2/0/w/200/h/200/format/png/interlace/1/"

