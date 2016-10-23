from HeZe.models import User


def revisepsw(UserPhone, OldPassWord, NewPassWord):
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