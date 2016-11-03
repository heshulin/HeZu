from django.http import HttpResponse
from HeZe.controller.userservice.login import dologin
from HeZe.controller.userservice.register import registe
from django.views.decorators.csrf import csrf_exempt
from HeZe.controller.userservice.revisepsw import revisepsw, Resetpsw
from HeZe.controller.userservice.logout import logout
from HeZe.controller.userservice.revisephoto import revisephoto
import json


# Create your views here.

#登录模块
@csrf_exempt
def login(request):
    try:
        UserPhone = request.POST.get('UserPhone')
        PassWord = request.POST.get('PassWord')
        print(UserPhone)
        result = json.dumps(dologin(UserPhone, PassWord))
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
    except Exception as e:
        print(e)
        response = HttpResponse('服务器异常')
    return response


@csrf_exempt
def logout(request):
    try:
        UserPhone = request.POST.get('UserPhone')
        SecretKey = request.POST.get('SecretKey')
        result = json.dumps(logout(UserPhone,SecretKey))
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
    except Exception as e:
        print(e)
        response = HttpResponse('服务器异常')
    return response
#end


#注册模块
@csrf_exempt
def sendmessage(request):
    try:
        UserPhone = request.POST.get('UserPhone')
        r = registe()
        result = json.dumps(r.sendmessage(UserPhone))
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
    except Exception as e:
        print(e)
        response = HttpResponse('服务器异常')
    return response


@csrf_exempt
def reg(request):
    try:
        UserPhone = request.POST.get('UserPhone')
        NickName = request.POST.get('NickName')
        CheckCode = request.POST.get('CheckCode')
        PassWord = request.POST.get('PassWord')
        r = registe()
        result = json.dumps(r.sendcheckcode(UserPhone, CheckCode, NickName, PassWord))
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
    except Exception as e:
        print(e)
        response = HttpResponse('服务器异常')
    return response
#end


#修改资料模块
@csrf_exempt
def revisepsw(request):
    try:
        UserPhone = request.POST.get('UserPhone')
        OldPassWord = request.POST.get('OldPassWord')
        NewPassWord = request.POST.get('NewPassWord')
        result = json.dumps(revisepsw(UserPhone,OldPassWord,NewPassWord))
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
    except Exception as e:
        print(e)
        response = HttpResponse('服务器异常')
    return response


@csrf_exempt
def revisephoto(request):
    try:
        UserPhoto = request.FILES['UserPhoto']
        UserPhone = request.POST.get('UserPhone')
        SecretKey = request.POST.get('SecretKey')
        result = json.dumps(revisephoto(UserPhone, SecretKey, UserPhoto))
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
    except Exception as e:
        print(e)
        response = HttpResponse('服务器异常')
    return response


@csrf_exempt
def resetpsw(request):
    try:
        UserPhone = request.POST.get('UserPhone')
        PassWord = request.POST.get('PassWord')
        CheckCode = request.POST.get('CheckCode')
        result = json.dumps(Resetpsw(UserPhone, CheckCode, PassWord))
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
    except Exception as e:
        print(e)
        response = HttpResponse('服务器异常')
    return response
#end



