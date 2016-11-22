from HeZe.models import SendHezu
from HeZe.bean.upimage import upimage
from HeZe.controller.userservice.personalinfo import getpersonalinfo
from django.core.paginator import Paginator, EmptyPage
from HeZe.bean.lbs_amap import get_distance
from django.forms.models import model_to_dict
import datetime

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
                    s.SendTime = str(datetime.datetime.now())
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
            array = {
                'msg': msg,
                'state': state
            }
            return array
        except Exception as e:
            print(e)
            array = {
                'msg': '服务器错误',
                'state': 0
            }
            return  array

    def allinfors(self, page):
        try:
            res = SendHezu.objects.filter(Delete=0).order_by('-SendHezuId').all()
            for i in res:
                state, distance = get_distance('111.688844,40.814395', i.Lon_Lat)
                i.Distance = distance
                i.save_base()
            page = int(page)
            s1 = res.order_by('Distance')
            s = Paginator(s1, 20).page(page)
            msg = '成功'
            state = 1
            num = len(s)
            if num > 0:
                hezudata = []
                for i in s:
                    res = getpersonalinfo(i.UserId)
                    arr = {
                        'SendHezuId': i.SendHezuId,
                        'UserId': i.UserId,
                        'Information': i.Information,
                        'Address': i.Address,
                        'Picture': i.Picture,
                        'SendTime': i.SendTime,
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
            array = {
                'state': state,
                'msg': msg,
                'hezudata': hezudata,
                'num': num
            }
            return array
        except EmptyPage:
            array = {
                'msg': '这是我的底线',
                'state': 0
            }
            return array
        except Exception as e:
            print(e)
            array = {
                'msg': '服务器异常',
                'state': 0
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
            array = {
                'state': state,
                'msg': msg
            }
            return array
        except Exception as e:
            print(e)
            state = 0
            msg = '服务器错误'
            array = {
                'state': state,
                'msg': msg
            }
            return array

    def selectInfors(self, Label1, Label2, Number, page):
        try:
            page = int(page)
            if Label1:
                lab1_arr = Label1.split('+')
                s1 = SendHezu.objects.filter(Label1__in=lab1_arr).order_by('-SendHezuId').all()
                hezudata = s1
                if Label2:
                    lab2_arr = Label2.split('+')
                    s2 = s1.filter(Label2__in=lab2_arr).order_by('-SendHezuId').all()
                    hezudata = s2
                    if Number:
                        num_arr = Number.split('+')
                        s3 = s2.filter(Number__in=num_arr).order_by('-SendHezuId').all()
                        hezudata = s3
                    else:
                        hezudata = s2
                else:
                    if Number:
                        num_arr = Number.split('+')
                        s3 = s1.filter(Number__in=num_arr).order_by('-SendHezuId').all()
                        hezudata = s3
                    else:
                        hezudata = s1

            else:
                if Label2:
                    lab2_arr = Label2.split('+')
                    s2 = SendHezu.objects.filter(Label2__in=lab2_arr).order_by('-SendHezuId').all()
                    hezudata = s2
                    if Number:
                        num_arr = Number.split('+')
                        s3 = s2.filter(Number__in=num_arr).order_by('-SendHezuId').all()
                        hezudata = s3
                    else:
                        hezudata = s2
                else:
                    if Number:
                        num_arr = Number.split('+')
                        s3 = SendHezu.objects.filter(Number__in=num_arr).order_by('-SendHezuId').all()
                        hezudata = s3
                    else:
                        hezudata = None
                hezudata = Paginator(hezudata, 20).page(page)
                msg = '成功'
                state = 1
                num = len(hezudata)
                data = []
                if num > 0:
                    for i in hezudata:
                        res = getpersonalinfo(i.UserId)
                        arr = {
                            'UserId': i.UserId,
                            'Information': i.Information,
                            'Address': i.Address,
                            'Picture': i.Picture,
                            'SendTime': i.SendTime,
                            'PictureEx': i.Picture.replace('?imageView2/0/w/200/h/200/format/png/interlace/1/', ''),
                            'Number': i.Number,
                            'UserPhoto': res['UserPhoto'],
                            'UserPhotoEx': res['UserPhotoEx'],
                            'NickName': res['NickName'],
                            'Label1': res['Label1'],
                            'Label2': res['Label2'],
                            'Label3': res['Label3']
                        }
                        data.append(arr)
                array = {
                    'hezudata': data,
                    'msg': msg,
                    'state': state,
                    'num': num
                }
                return array
        except EmptyPage:
            array = {
                'msg': '这是我的底线',
                'state': 0
            }
            return array
        except Exception as e:
            print(e)
            array = {
                'msg': '服务异常',
                'state': 0
            }
            return array

    def thishezu(self, SendHezuId):
        try:
            s = SendHezu.objects.get(SendHezuId=SendHezuId)
            UserId = s.UserId
            arr = model_to_dict(s)
            personalinfor = getpersonalinfo(UserId)
            arr['PictureEx'] = s.Picture.replace('?imageView2/0/w/200/h/200/format/png/interlace/1/', '')
            arr['UserPhoto'] = personalinfor['UserPhoto']
            arr['UserPhotoEx'] = personalinfor['UserPhoto']
            arr['NickName'] = personalinfor['NickName']
            arr['Label3'] = personalinfor['Label3']
            array = {
                'msg': '成功',
                'state': 1,
                'hezudata': arr
            }
            return array
        except Exception as e:
            print(e)
            array = {
                'msg': '服务异常',
                'state': 0
            }
            return array


