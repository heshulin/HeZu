from HeZe.controller.userservice.islog import islog
from HeZe.bean.upimage import upimage


def revisePhoto(UserPhone, SecretKey, UserPhoto):
    try:
        state, user = islog(UserPhone, SecretKey)
        if state == 1:
            uu = upimage()
            a = uu.upuserphoto(UserPhoto, 'hezu')
            if a['state'] == 1:
                path = a['url']
                user.UserPhoto = path
                user.save()
                msg = '修改成功'
                state = 1
            else:
                msg = a['msg']
                state = 0
        else:
            state= 0
            msg = '请登录'
    except Exception as e:
        print(e)
        state = 0
        msg = '服务器异常'
    array = {
        'msg': msg,
        'state': state
    }
    return array