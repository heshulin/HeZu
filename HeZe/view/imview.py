from django.http import HttpResponse
from HeZe.controller.imservice.attention import Attentionservice
from HeZe.controller.imservice.im import Imservice
from django.views.decorators.csrf import csrf_exempt
from HeZe.controller.userservice.islog import islog
import json

@csrf_exempt
def getfriends(request):
    try:
        i = Imservice()
        UserPhone = request.POST.get('UserPhone')
        SecretKey = request.POST.get('SecretKey')
        state, user = islog(UserPhone, SecretKey)
        if state == 1:
            result = json.dumps(i.getfriends(UserPhone=UserPhone,SecretKey=SecretKey))
        else:
            result = json.dumps({'state': 0, 'msg': '请登录'})
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
    except Exception as e:
        print(e)
        response = HttpResponse('服务器异常')
    return response


@csrf_exempt
def attention(request):
    try:
        a = Attentionservice()
        UserPhone = request.POST.get('UserPhone')
        SecretKey = request.POST.get('SecretKey')
        BefocusonId = request.POST.get('BefocusonId')
        state, user = islog(UserPhone, SecretKey)
        if state == 1:
            result = json.dumps(a.attention_other(UserPhone=UserPhone, SecretKey=SecretKey, BefocusonId=BefocusonId))
        else:
            result = json.dumps({'state': 0, 'msg': '请登录'})
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
    except Exception as e:
        print(e)
        response = HttpResponse('服务器异常')
    return response

@csrf_exempt
def gettoken(request):
    try:
        i = Imservice()
        UserPhone = request.POST.get('UserPhone')
        SecretKey = request.POST.get('SecretKey')
        state, user = islog(UserPhone, SecretKey)
        if state == 1:
            result = json.dumps(i.gettoken(UserPhone=UserPhone))
        else:
            result = json.dumps({'state': 0, 'msg': '请登录'})
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
    except Exception as e:
        print(e)
        response = HttpResponse('服务器异常')
    return response
