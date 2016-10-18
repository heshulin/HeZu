from HeZe.models import User


def dologin(UserPhone, PassWord):
    u = User.objects.filter(UserPhone=UserPhone, PassWord=PassWord)
    if not u:
        state = 0
        msg = '用户名或密码错误'
    else:
        state = 1
        msg = '登陆成功'
    array = {
        'state': state,
        'msg': msg
    }
    return array