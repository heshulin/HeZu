from HeZe.models import User
from HeZe.bean.md5 import encrypt
from HeZe.bean.secretkey import GetSecretKey
from HeZe.controller.imservice.im import Imservice

def getpersonalinfo(UserId):
    UserPhoto = ""
    NickName = ""
    Address = ""
    UserPhone = ""
    Label1 = ""
    Label2 = ""
    Label3 = ""
    try:
        u = User.objects.get(UserId=UserId)
        if u:
            UserPhoto = u.UserPhoto
            NickName = u.NickName
            Address = u.Address
            UserPhone = u.UserPhone
            Label1 = u.Label1
            Label2 = u.Label2
            Label3 = u.Label3
            msg = '成功'
            state = 1
        else:
            state = 0
            msg = '操作非法'
    except Exception as e:
        print(e)
        state = 0
        msg = '服务器异常'
    array = {
        'UserPhoto': UserPhoto,
        'NickName':NickName,
        'Address':Address,
        'UserPhone':UserPhone,
        'Label1':Label1,
        'Label2':Label2,
        'Label3':Label3,
        'msg': msg,
        'state': state
    }
    return array