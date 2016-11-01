from HeZe.models import Circle,User,CircleComment
from HeZe.bean.upimage import upimage

class circle():
    def sendcircle(self, UserId, Information, Picture):
        try:
            if UserId and Information and Picture:
                uu = upimage()
                arr = uu.upuserphoto(Picture, 'hezu')
                if arr['state']:
                    s = Circle()
                    s.UserId = UserId
                    s.Information = Information
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
                    'Picture': i.Picture,
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




