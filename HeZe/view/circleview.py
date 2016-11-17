from django.http import HttpResponse
from HeZe.controller.userservice.islog import islog
from HeZe.controller.circleservice.circle import circle
from django.views.decorators.csrf import csrf_exempt
import json


#发朋友圈
@csrf_exempt
def sendcircle(request):
    try:
        UserPhone = request.POST.get('UserPhone')
        SecretKey = request.POST.get('SecretKey')
        Information = request.POST.get('Information')
        Title = request.POST.get('Title')
        num = request.POST.get('num')
        Picture = []
        for i in range(1, int(num)+1):
            Picture.append(request.FILES['Picture'+str(i)])
        state, user = islog(UserPhone, SecretKey)
        if state == 1:
            C = circle()
            result = json.dumps(C.sendcircle(user.UserId, Information, Title, Picture, num))
        else:
            result = json.dumps({'state': 0, 'msg': '请登录'})
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)
        result = {
            'msg': '请求异常',
            'state': 0
        }
        result = json.dumps(result)
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        return response
#end

#朋友圈首页信息
@csrf_exempt
def circleinfo(request):
    try:
        C = circle()
        result = json.dumps(C.getinfo())
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)
        result = {
            'msg': '请求异常',
            'state': 0
        }
        result = json.dumps(result)
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
        return response
#end


#朋友圈单个信息
@csrf_exempt
def circleoneinfo(request):
    try:
        UserPhone = request.GET.get('UserPhone')
        SecretKey = request.GET.get('SecretKey')
        CircleId = request.GET.get('CircleId')
        state, user = islog(UserPhone, SecretKey)
        if state == 1:
            C = circle()
            result = json.dumps(C.getoneinfo(CircleId=CircleId))
        else:
            result = json.dumps({'state': 0, 'msg': '请登录'})
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
    except Exception as e:
        print(e)
        response = HttpResponse('服务器异常')
    return response
#end

#朋友圈发布评论
@csrf_exempt
def sendcomment(request):
    try:
        UserPhone = request.GET.get('UserPhone')
        SecretKey = request.GET.get('SecretKey')
        CircleId = request.GET.get('CircleId')
        Comment = request.GET.get('Comment')
        state, user = islog(UserPhone, SecretKey)
        if state == 1:
            C = circle()
            result = json.dumps(C.sendcommit(UserId=user.UserId,CircleId=CircleId,Comment=Comment))
        else:
            result = json.dumps({'state': 0, 'msg': '请登录'})
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
    except Exception as e:
        print(e)
        response = HttpResponse('服务器异常')
    return response
#end


#朋友圈评论信息
@csrf_exempt
def commentinfo(request):
    try:
        UserPhone = request.GET.get('UserPhone')
        SecretKey = request.GET.get('SecretKey')
        CircleId = request.GET.get('CircleId')
        state, user = islog(UserPhone, SecretKey)
        if state == 1:
            C = circle()
            result = json.dumps(C.getcommit(CircleId=CircleId))
        else:
            result = json.dumps({'state': 0, 'msg': '请登录'})
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
    except Exception as e:
        print(e)
        response = HttpResponse('服务器异常')
    return response
#end