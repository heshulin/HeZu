from HeZe.models import Circle,User,CircleComment
from HeZe.bean.upimage import upimage
from HeZe.controller.userservice.personalinfo import getpersonalinfo
import datetime
from django.core.paginator import Paginator, EmptyPage


class circle():
    def sendcircle(self, UserId, Information,Title, Picture, num):
        try:
            if UserId and Information:
                uu = upimage()
                s = Circle()
                s.Title = Title
                s.UserId = UserId
                s.Information = Information
                s.SendTime = str(datetime.datetime.now())
                picture_path = ''
                if int(num) > 0:
                    for i in Picture:
                        arr1 = uu.upuserphoto(i, 'hezu')
                        if arr1['state']:
                            picture_path = picture_path + arr1['url'] + '+'
                s.Picture = picture_path
                s.save()
                state = 1
                msg = '成功'
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
            state = 0
            msg = '失败'
            array = {
                'msg': msg,
                'state': state
            }
            return array

    def getinfo(self, page):
        try:
            s1 = Circle.objects.filter().order_by('-CircleId').all()
            s = Paginator(s1, 20).page(page)
            msg = '成功'
            state = 1
            num = len(s)
            circledata = []
            for i in s:
                u = getpersonalinfo(i.UserId)
                Picture = i.Picture.replace('?imageView2/0/w/200/h/200/format/png/interlace/1/', '')
                arr = {
                    'UserId': i.UserId,
                    'Title': i.Title,
                    'CircleId': i.CircleId,
                    'NickName': u['NickName'],
                    'UserPhoto': u['UserPhoto'],
                    'UserPhotoEx': u['UserPhotoEx'],
                    'SendTime': i.SendTime,
                    'Picture': i.Picture.split('+'),
                    'PictureEx': Picture.split('+'),
                    'Label1': u['Label1'],
                    'Label2': u['Label2'],
                    'Label3': u['Label3'],
                    'Information': i.Information,
                }
                circledata.append(arr)
        except EmptyPage:
            array = {
                'msg': '这是我的底线',
                'state': 0
                }
            return array
        except Exception as e:
            print(e)
            msg = '服务器错误'
            state = 0
            circledata = None
            num = 0
        array = {
            'msg': msg,
            'state': state,
            'circledata': circledata,
            'num': num
        }
        return array

    def sendcommit(self,UserId,CircleId,Comment):
        try:
            c = CircleComment()
            c.UserId = UserId
            c.CircleId = CircleId
            c.Comment = Comment
            c.save()
            state = 1
            msg = "评论成功"
        except Exception as e:
            print(e)
            msg = '服务器错误'
            state = 0

        array = {
            'msg': msg,
            'state': state,
        }
        return array

    def getoneinfo(self,CircleId):
        try:
            c = Circle.objects.filter(CircleId=CircleId).first()
            u = User.objects.filter(UserId=c.UserId).first()
            data = {
                'CircleId': c.CircleId,
                'Title': c.Title,
                'UserId': c.UserId,
                'NickName': u.NickName,
                'UserPhoto': u.UserPhoto,
                'Label1': u.Label1,
                'Label2': u.Label2,
                'Label3': u.Label3,
                'Information': c.Information,
                'SendTime': c.SendTime.split('.')[0],
                'Picture': c.Picture.split('+'),
            }
            state = 1
            msg = "成功"
            array = {
                'data': data,
                'msg': msg,
                'state': state,
            }
            return array
        except Exception as e:
            print(e)
            data = []
            msg = '服务器错误'
            state = 0
            array = {
                'data':data,
                'msg': msg,
                'state': state,
            }
            return array

    def getcommit(self,CircleId):
        try:
            c = CircleComment.objects.filter(CircleId=CircleId).all()
            data = []
            msg = '成功'
            state = 1
            num = len(c)
            for i in c:
                u = User.objects.filter(UserId=i.UserId).first()
                arr = {
                    'UserId': i.UserId,
                    'NickName': u.NickName,
                    'UserPhoto': u.UserPhoto,
                    'Label1': u.Label1,
                    'Label2': u.Label2,
                    'Label3': u.Label3,
                    'Comment': i.Comment,
                }
                data.append(arr)
        except Exception as e:
            print(e)
            msg = '服务器错误'
            state = 0
            data = None
            num = 0
        array = {
            'msg': msg,
            'state': state,
            'data': data,
            'num': num
        }
        return array




