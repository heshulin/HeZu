from HeZe.models import User
from HeZe.bean.md5 import encrypt
from HeZe.bean.secretkey import GetSecretKey
from HeZe.controller.imservice.im import Imservice


def dologin(UserPhone, PassWord):
    token = ""
    try:
        if UserPhone and PassWord:
            PassWord = encrypt(PassWord.encode('utf8'))
            u = User.objects.filter(UserPhone=UserPhone, PassWord=PassWord).first()
            if not u:
                state = 0
                msg = '用户名或密码错误'
                SecretKey = None
            else:
                IM = Imservice()
                token = IM.gettoken(UserPhone=UserPhone)
                SecretKey = GetSecretKey()
                u.SecretKey = SecretKey
                u.save()
                state = 1
                print("token")
                print(token)
                msg = '登陆成功'
        else:
            state = 0
            msg = '用户名密码不能为空'
            SecretKey = None
    except Exception as e:
        print(e)
        state = 0
        msg = '服务器异常'
        SecretKey = None
    array = {
        'token': token,
        'state': state,
        'msg': msg,
        'SecretKey': SecretKey
    }
    return array