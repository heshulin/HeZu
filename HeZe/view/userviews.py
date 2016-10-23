from django.http import HttpResponse
from HeZe.controller.userservice.login import dologin
from HeZe.controller.userservice.register import registe
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

#登录模块
@csrf_exempt
def login(request):
    try:
        UserPhone = request.POST.get('UserPhone')
        PassWord = request.POST.get('PassWord')
        result = json.dumps(dologin(UserPhone, PassWord))
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)
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
        return response
    except Exception as e:
        print(e)


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
        return response
    except Exception as e:
        print(e)
#end



