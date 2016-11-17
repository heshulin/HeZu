from django.http import HttpResponse
from HeZe.controller.userservice.islog import islog
from HeZe.controller.hezuservice.hezu import hezu
from django.views.decorators.csrf import csrf_exempt
import json


#发合租
@csrf_exempt
def sendhezu(request):
    try:
        UserPhone = request.POST.get('UserPhone')
        SecretKey = request.POST.get('SecretKey')
        Information = request.POST.get('Information')
        Address = request.POST.get('Address')
        Number = request.POST.get('Number')
        Picture = request.FILES['Picture']
        state, user = islog(UserPhone, SecretKey)
        if state == 1:
            h = hezu()
            result = json.dumps(h.sendhezu(user.UserId, Information, Address, Picture, Number))
        else:
            result = json.dumps({'state': 0, 'msg': '请登录'})
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)
        result = {
            'msg': '服务器错误',
            'state': 0
        }
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        return response
#end


#合租首页信息
@csrf_exempt
def hezuinfors(request):
    try:
        page = request.GET.get('page')
        if page:
            h = hezu()
            result = json.dumps(h.allinfors(page))
            response = HttpResponse(result, content_type="application/json")
            response["Access-Control-Allow-Origin"] = "*"
        else:
            result = {
                'msg': '请求异常',
                'state': 0
            }
            response = HttpResponse(result, content_type="application/json")
            response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)
        result = {
            'msg': '服务器错误',
            'state': 0
        }
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        return response


@csrf_exempt
def selectinfors(request):
    try:
        page = request.GET.get('page')
        Label1 = request.GET.get('Label1')
        Label2 = request.GET.get('Label2')
        Number = request.GET.get('Number')
        if page:
            h = hezu()
            result = json.dumps(h.selectInfors(Label1, Label2, Number, page))
            response = HttpResponse(result, content_type="application/json")
            response["Access-Control-Allow-Origin"] = "*"
        else:
            result = {
                'msg': '服务器错误',
                'state': 0
            }
            response = HttpResponse(result, content_type="application/json")
            response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)
        result = {
            'msg': '请求异常',
            'state': 0
        }
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        return response
#end


#撤销合租
@csrf_exempt
def canclehezu(request):
    try:
        UserPhone = request.POST.get('UserPhone')
        SecretKey = request.POST.get('SecretKey')
        SendHezuId = request.POST.get('SendHezuId')
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
        return response
    except Exception as e:
        print(e)
        result = {
            'msg': '服务器错误',
            'state': 0
        }
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        return response
#end


@csrf_exempt
def get_thishezu(request):
    try:
        SendHezuId = request.GET.get('SendHezuId')
        h = hezu()
        result = json.dumps(h.thishezu(SendHezuId))
        response = HttpResponse(result, content_type='application/json')
        return response
    except Exception as e:
        print(e)
        result = {
            'msg': '服务器错误',
            'state': 0
        }
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        return response

