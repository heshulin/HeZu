from HeZe.models import User, Checkcode
import datetime
from HeZe.bean.md5 import encrypt


def Revisepsw(UserPhone, OldPassWord, NewPassWord):
    try:
        u = User.objects.get(UserPhone=UserPhone, PassWord=OldPassWord)
        if u:
            u.PassWord = NewPassWord
            u.SecretKey = ''
            u.save()
            state = 1
            msg = '修改成功，请重新登陆'
        else:
            state = 0
            msg = '密码错误'
    except Exception as e:
        print(e)
        msg = '服务器异常'
        state = 0
    array = {
        'state': state,
        'msg': msg
    }
    return array


def Resetpsw(self, UserPhone, CheckCode, PassWord):
    try:
        if UserPhone and Checkcode and PassWord:
            c = Checkcode.objects.filter(UserPhone=UserPhone, CheckCode=CheckCode).order_by('-CheckCodeId').first()
            t = datetime.datetime.now() - datetime.timedelta(minutes=3)
            if c:
                c.SendTime = c.SendTime.replace(tzinfo=None)
                if t > c.SendTime:
                    msg = '验证码已过期'
                    state = 0
                else:
                    u = User.objects.get(UserPhone=UserPhone)
                    u.PassWord = encrypt(PassWord.encode('utf8'))
                    u.save()
                    msg = '成功'
                    state = 1
            else:
                msg = '验证码不正确'
                state = 0
        else:
            msg = '密码不能为空'
            state = 0
    except Exception as e:
        print(e)
        msg = '服务器错误'
        state = 0
    array = {
        'msg': msg,
        'state': state
    }
    return array
