import os
from HeZe.bean.rong import ApiClient
from flask import request
from HeZe.models import User, Attention


class Imservice(object):
    def gettoken(self,UserPhone):
        try:
            user = User.objects.filter(UserPhone=UserPhone).first()
            if user.Token != None:
                return user.Token
            app_key = 'y745wfm8440uv'
            app_secret = '8H4Zs6MenT3Trf'
            api = ApiClient(app_key, app_secret)
            r = api.getToken(userId=user.UserId, name=user.NickName,portraitUri=user.UserPhoto)
            r = str(r)
            r = eval(r)
            user.Token = r['token']
            user.save()
            return r['token']
        except Exception as e:
            return "失败"

    def getfriends(self,UserPhone,SecretKey):
        try:

            user = User.objects.filter(UserPhone=UserPhone).first()
            if SecretKey == user.SecretKey:
                friends = Attention.objects.filter(UserId=user.UserId).all()
                data = []
                if len(friends)==0:
                    array = {
                    'state':1,
                    'msg':"没有好友",
                    'data':[]
                    }
                    return array
                for i in range(0,len(friends)):
                    array = {}
                    user1 = User.query.filter_by(UserId=friends[i].BefocusonId).first()
                    array['UserId'] = user1.UserId
                    array['NickName'] = user1.NickName
                    array['UserPhone'] = user1.UserPhone
                    array['UserPhoto'] = user1.UserPhoto
                    array['UserSex'] = user1.UserSex
                    array['UserMajor'] = user1.UserMajor
                    array['UserGrade'] = user1.UserGrade
                    data.append(array)
                array = {
                    'state': 1,
                    'msg': "成功",
                    'data': data
                }
                return array
            else:
                array = {
                    'state' : 0,
                    'msg' : "请登录后再重新尝试",
                }
                return array
        except Exception as e:
            array = {
                'state': 0,
                'msg': "失败",
            }
            return array