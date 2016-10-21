from HeZe.models import User, Checkcode
from HeZe.bean.message import Message
import re
import datetime
from HeZe.bean.md5 import encrypt


class registe():

    def sendmessage(self, UserPhone):
        try:
            if UserPhone:
                p = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
                p1 = p.match(UserPhone)
                if p1:
                    m = Message()
                    checkcode = m.sendMessage(UserPhone)
                    c = Checkcode()
                    c.UserPhone = UserPhone
                    c.CheckCode = checkcode
                    c.SendTime = datetime.datetime.now() + datetime.timedelta(hours=8)
                    c.save()
                    msg = '验证码已发送'
                    state = 1
                else:
                   msg = '请输入正确的手机号'
                   state = 0
            else:
                msg = '请输入正确的手机号'
                state = 0
        except Exception as e:
            print(e)
            msg = '服务器异常'
            state = 0
        array = {
            'msg': msg,
            'state': state
        }
        return array

    def sendcheckcode(self, UserPhone, CheckCode, NickName, PassWord):
        try:
            if UserPhone and Checkcode and NickName and PassWord:
                c = Checkcode.objects.filter(UserPhone=UserPhone, CheckCode=CheckCode).order_by('-CheckCodeId').first()
                t = datetime.datetime.now() + datetime.timedelta(hours=8) - datetime.timedelta(minutes=3)
                if c:
                    c.SendTime = c.SendTime.replace(tzinfo=None)
                    if t > c.SendTime:
                        msg = '验证码已过期'
                        state = 0
                    else:
                        u = User()
                        u.UserPhone = UserPhone
                        u.PassWord = encrypt(PassWord)
                        u.Label1 = '0'
                        u.Label2 = '0'
                        u.Label3 = '0'
                        u.NickName = NickName
                        u.UserPhoto = ' '
                        u.Address = ' '
                        u.SecretKey = ' '
                        u.save()
                        msg = '注册成功'
                        state = 1
                else:
                    msg = '验证码不正确'
                    state = 0
            else:
                msg = '信息不能为空'
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