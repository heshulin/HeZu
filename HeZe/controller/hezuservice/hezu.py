from HeZe.models import SendHezu
from HeZe.bean.upimage import upimage

class hezu():
    def sendhezu(self, UserId, Information, Address, Picture, Number):
        try:
            if Information and Address and Picture and Number:
                uu = upimage()
                arr = uu.upuserphoto(Picture,'hezu')
                if arr['state']:
                    s = SendHezu()
                    s.UserId = UserId
                    s.Information = Information
                    s.Address =Address
                    s.Number = int(Number)
                    s.Delete = 0
                    s.Picture = arr['url']
                    s.save()
                    state = 1
                    msg = '成功'
                else:
                    state = 0
                    msg = '服务器错误'
            else:
                state = 0
                msg = '信息不能为空'
        except Exception as e:
            print(e)
            state = 0
            msg = '失败'
        array = {
            'msg': msg,
            'state': state
        }
        return  array
    def allinfors(self):
        try:
            s = SendHezu.objects.filter().order_by('-SendHezuId').all()
            msg = '成功'
            state = 1
            num = len(s)
            hezudata = []
            for i in s:
                arr = {
                    'UserId': i.UserId,
                    'Information': i.Information,
                    'Address': i.Address,
                    'Picture': i.Picture,
                    'Number': i.Number
                }
                hezudata.append(arr)
        except Exception as e:
            print(e)
            msg = '服务器错误'
            state = 0
            hezudata = None
            num = 0
        array = {
            'msg': msg,
            'state': state,
            'hezudata': hezudata,
            'num': num
        }
        return array
    def delhezu(self, UserPhone, SecretKey, SendHeZuId):
        pass


