from HeZe.models import User
from HeZe.bean.lbs_amap import get_hint


def doLocate(Lon_Lat, Address, UserPhone, SecretKey):
    try:
        u = User.objects.filter(UserPhone=UserPhone, SecretKey=SecretKey).first()
        if u:
            if Lon_Lat and Address:
                u.Address = Address
                u.Lon_Lat = Lon_Lat
                u.save()
                msg = '定位成功'
                state = 1
            else:
                msg = '定位失败'
                state = 0
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


def getHint(keywords):
    try:
        if keywords:
            res = get_hint(keywords)
            if res['status'] == '1':
                msg = '成功'
                state = 1
                tips = []
                del res['tips'][0]
                for i in res['tips']:
                    arr = {
                        'placename': i['name'],
                        'address': str(i['district']) + str(i['address']),
                        'location': str(i['location'])
                    }
                    tips.append(arr)
                num = int(res['count']) - 1
            else:
                msg = '没有找到相关结果'
                state = 0
                tips = None
                num = 0
            array = {
                'msg': msg,
                'state': state,
                'tips': tips,
                'num': num
            }
            return array
        else:
            array = {
                'msg': '没有相关提示',
                'state': 1,
            }
            return array
    except Exception as e:
        array = {
            'msg': '服务器错误',
            'state': 0
        }
        return array
