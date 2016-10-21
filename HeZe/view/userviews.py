from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from HeZe.controller.userservice.login import dologin
from HeZe.controller.userservice.register import registe
import json

# Create your views here.

#登录模块
def login(request):
    try:
        UserPhone = request.GET.get('UserPhone')
        PassWord = request.GET.get('PassWord')
        result = json.dumps(dologin(UserPhone, PassWord))
        response = HttpResponse(result, content_type="application/json")
        return response
    except Exception as e:
        print(e)
#end


#注册模块
def sendmessage(request):
    try:
        UserPhone = request.GET.get('UserPhone')
        r = registe()
        result = json.dumps(r.sendmessage(UserPhone))
        return HttpResponse(result, content_type="application/json")
    except Exception as e:
        print(e)


def reg(request):
    try:
        UserPhone = request.GET.get('UserPhone')
        NickName = request.GET.get('NickName')
        CheckCode = request.GET.get('CheckCode')
        PassWord = request.GET.get('PassWord')
        r = registe()
        result = json.dumps(r.sendcheckcode(UserPhone, CheckCode, NickName, PassWord))
        return HttpResponse(result, content_type="application/json")
    except Exception as e:
        print(e)
#end



