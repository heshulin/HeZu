from HeZe.models import Circle,User,CircleComment
from HeZe.bean.upimage import upimage
import time

class circle():
    def sendcircle(self, UserId, Information,Title, Picture1, Picture2, Picture3, Picture4, Picture5, Picture6,
                   Picture7, Picture8, Picture9):
        try:
            if UserId and Information:
                uu = upimage()
                s = Circle()
                s.Title = Title
                s.UserId = UserId
                s.Information = Information
                ISOTIMEFORMAT = '%Y-%m-%d %X'
                s.time = time.strftime(ISOTIMEFORMAT, time.localtime())
                if Picture1:
                    arr1 = uu.upuserphoto(Picture1, 'hezu')
                    if arr1['state']:
                        s.Picture1 = arr1['url']
                else:
                    s.Picture1 = ""
                if Picture2:
                    arr2 = uu.upuserphoto(Picture2, 'hezu')
                    if arr2['state']:
                        s.Picture2 = arr2['url']

                else:
                    s.Picture2 = ""

                if Picture3:
                    arr2 = uu.upuserphoto(Picture3, 'hezu')
                    if arr2['state']:
                        s.Picture3 = arr2['url']

                else:
                    s.Picture3 = ""

                if Picture4:
                    arr2 = uu.upuserphoto(Picture4, 'hezu')
                    if arr2['state']:
                        s.Picture4 = arr2['url']

                else:
                    s.Picture4 = ""

                if Picture5:
                    arr2 = uu.upuserphoto(Picture5, 'hezu')
                    if arr2['state']:
                        s.Picture5 = arr2['url']

                else:
                    s.Picture5 = ""

                if Picture6:
                    arr2 = uu.upuserphoto(Picture6, 'hezu')
                    if arr2['state']:
                        s.Picture6 = arr2['url']

                else:
                    s.Picture6 = ""

                if Picture7:
                    arr2 = uu.upuserphoto(Picture7, 'hezu')
                    if arr2['state']:
                        s.Picture7 = arr2['url']

                else:
                    s.Picture7 = ""

                if Picture8:
                    arr2 = uu.upuserphoto(Picture8, 'hezu')
                    if arr2['state']:
                        s.Picture8 = arr2['url']

                else:
                    s.Picture8 = ""

                if Picture9:
                    arr2 = uu.upuserphoto(Picture9, 'hezu')
                    if arr2['state']:
                        s.Picture9 = arr2['url']

                else:
                    s.Picture9 = ""

                state = 1
                msg = '成功'
                s.save()


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
        return array

    def getinfo(self):
        try:
            s = Circle.objects.filter().order_by('-CircleId').all()
            msg = '成功'
            state = 1
            num = len(s)
            circledata = []
            for i in s:
                u = User.objects.filter(UserId=i.UserId).first()
                arr = {
                    'UserId': i.UserId,
                    'CircleId':i.CircleId,
                    'NickName':u.NickName,
                    'UserPhoto':u.UserPhoto,
                    'Label1':u.Label1,
                    'Label2': u.Label2,
                    'Label3': u.Label3,
                    'Information': i.Information,
                    'Picture1': i.Picture1,
                    'Picture2': i.Picture2,
                    'Picture3': i.Picture3,
                    'Picture4': i.Picture4,
                    'Picture5': i.Picture5,
                    'Picture6': i.Picture6,
                    'Picture7': i.Picture7,
                    'Picture8': i.Picture8,
                    'Picture9': i.Picture9,
                }
                circledata.append(arr)
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
                'UserId': c.UserId,
                'NickName': u.NickName,
                'UserPhoto': u.UserPhoto,
                'Label1': u.Label1,
                'Label2': u.Label2,
                'Label3': u.Label3,
                'Information': c.Information,
                'Picture':c.Picture
            }
            state = 1
            msg = "成功"
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
                u = User.objects.filter(UserId=c.UserId).first()
                arr = {
                    'UserId': c.UserId,
                    'NickName': u.NickName,
                    'UserPhoto': u.UserPhoto,
                    'Label1': u.Label1,
                    'Label2': u.Label2,
                    'Label3': u.Label3,
                    'Comment': c.Comment,
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




