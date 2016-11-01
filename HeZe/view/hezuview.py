from django.http import HttpResponse
from HeZe.controller.userservice.islog import islog
from HeZe.controller.hezuservice.hezu import hezu
from django.views.decorators.csrf import csrf_exempt
import json


#发合租
@csrf_exempt
def sendhezu(request):
    try:
        UserPhone = request.GET.get('UserPhone')
        SecretKey = request.GET.get('SecretKey')
        Information = request.GET.get('Information')
        Address = request.GET.get('Address')
        Number = request.GET.get('Number')
        Picture = request.FILES['Picture']
        state, user = islog(UserPhone, SecretKey)
        if state == 1:
            h = hezu()
            result = json.dumps(h.sendhezu(user.UserId, Information, Address, Picture, Number))
        else:
            result = json.dumps({'state': 0, 'msg': '请登录'})
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
    except Exception as e:
        print(e)
        response = HttpResponse('服务器异常')
    return response
#end


#合租首页信息
@csrf_exempt
def hezuinfors(request):
    try:
        h = hezu()
        result = json.dumps(h.allinfors())
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
    except Exception as e:
        print(e)
        response = HttpResponse('服务器异常')
    return response
#end


#撤销合租
@csrf_exempt
def canclehezu(request):
    try:
        UserPhone = request.GET.get('UserPhone')
        SecretKey = request.GET.get('SecretKey')
        SendHezuId = request.GET.get('SendHezuId')
        state, user = islog(UserPhone, SecretKey)
        if state == 1:
            h = hezu()
            array = h.canclehezu(user.UserId, SendHezuId)
        else:
            array = {
                'state': 0,
                'msg': '请登录'
            }
        result = json.dumps(array)
        response = HttpResponse(result, content_type='application/json')
    except Exception as e:
        print(e)
        response = HttpResponse('服务器异常')
    return response
#end
