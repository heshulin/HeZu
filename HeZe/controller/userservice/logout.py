from HeZe.models import User


def logout(UserPhone, SecretKey):
    try:
        u = User.objects.get(UserPhone=UserPhone, SecretKey=SecretKey)
        if u:
            u.SecretKey = ''
            u.save()
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
        'msg': msg,
        'state': state
    }
    return array

