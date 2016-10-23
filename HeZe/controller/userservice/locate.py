from HeZe.controller.userservice.islog import islog


def doLocate(Adress, UserPhone, SecretKey):
    try:
        state, user = islog(UserPhone, SecretKey)
        if state == 1:
            u = user
            u.Adress = Adress
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
