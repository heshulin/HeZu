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
        UserPhone = request.POST.get('UserPhone')
        PassWord = request.POST.get('PassWord')
        result = json.dumps(dologin(UserPhone, PassWord))
        return HttpResponse(result, content_type="application/json")
    except Exception as e:
        print(e)
#end


#注册模块
def sendmessage(request):
    try:
        UserPhone = request.POST.get('UserPhone')
        r = registe()
        result = json.dumps(r.sendmessage(UserPhone))
        return HttpResponse(result, content_type="application/json")
    except Exception as e:
        print(e)


def reg(request):
    try:
        UserPhone = request.POST.get('UserPhone')
        NickName = request.POST.get('NickName')
        CheckCode = request.POST.get('CheckCode')
        PassWord = request.POST.get('PassWord')
        r = registe()
        result = json.dumps(r.sendcheckcode(UserPhone, CheckCode, NickName, PassWord))
        return HttpResponse(result, content_type="application/json")
    except Exception as e:
        print(e)
#end



