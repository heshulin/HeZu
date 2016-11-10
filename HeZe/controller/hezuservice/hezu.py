from HeZe.models import SendHezu
from HeZe.bean.upimage import upimage
from HeZe.controller.userservice.personalinfo import getpersonalinfo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class hezu():

    def sendhezu(self, UserId, Information, Address, Picture, Number):
        try:
            if Information and Address and Picture and Number:
                uu = upimage()
                arr = uu.upuserphoto(Picture, 'hezu')
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

    def allinfors(self, page):
        try:
            page = int(page)
            s1 = SendHezu.objects.filter().order_by('-SendHezuId').all()
            s = Paginator(s1, 20).page(page)
            msg = '成功'
            state = 1
            num = len(s)
            if num > 0:
                hezudata = []
                for i in s:
                    res = getpersonalinfo(i.UserId)
                    arr = {
                        'UserId': i.UserId,
                        'Information': i.Information,
                        'Address': i.Address,
                        'Picture': i.Picture,
                        'PictureEx': i.Picture.replace('?imageView2/0/w/200/h/200/format/png/interlace/1/', ''),
                        'Number': i.Number,
                        'UserPhoto': res['UserPhoto'],
                        'UserPhotoEx': res['UserPhotoEx'],
                        'NickName': res['NickName'],
                        'Label1': res['Label1'],
                        'Label2': res['Label2'],
                        'Label3': res['Label3'],
                    }
                    hezudata.append(arr)
            else:
                hezudata = None
                num = 0
        except EmptyPage:
            msg = '这是我的底线'
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

    def canclehezu(self, UserId, SendHeZuId):
        try:
            if SendHeZuId:
                s = SendHezu.objects.filter(SendHeZuId=SendHeZuId, UserId=UserId).first()
                if s:
                    if s.Delete == 0:
                        s.Delete = 1
                        s.save()
                        state = 1
                        msg = '撤销成功'
                    else:
                        state = 1
                        msg = '撤销成功'
                else:
                    state = 0
                    msg = '操作非法'
            else:
                state = 0
                msg = '请登录'
        except Exception as e:
            print(e)
            state = 0
            msg = '服务器错误'
        array = {
            'state': state,
            'msg': msg
        }
        return array



