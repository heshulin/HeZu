from HeZe.models import User


def doLocate(Adress, UserPhone, SecretKey):
    try:
        u = User.objects.filter(UserPhone=UserPhone, SecretKey=SecretKey).first()
        if u:
            u.Address = Adress
            u.save()
            msg = '定位成功'
            state = 1
        else:
            msg = '请登录'
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
