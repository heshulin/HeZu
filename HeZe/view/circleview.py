from django.http import HttpResponse
from HeZe.controller.userservice.islog import islog
from HeZe.controller.circleservice.circle import circle
from django.views.decorators.csrf import csrf_exempt
import json


#发朋友圈
@csrf_exempt
def sendcircle(request):
    try:
        UserPhone = request.GET.get('UserPhone')
        SecretKey = request.GET.get('SecretKey')
        Information = request.GET.get('Information')
        Title = request.GET.get('Information')
        Picture1 = request.FILES['Picture']
        Picture2 = request.FILES['Picture']
        Picture3 = request.FILES['Picture']
        Picture4 = request.FILES['Picture']
        Picture5 = request.FILES['Picture']
        Picture6 = request.FILES['Picture']
        Picture7 = request.FILES['Picture']
        Picture8 = request.FILES['Picture']
        Picture9 = request.FILES['Picture']

        state, user = islog(UserPhone, SecretKey)
        if state == 1:
            C = circle()
            result = json.dumps(C.sendcircle(UserId=user.UserId,Information=Information,Title=Title,Picture1=Picture1,
                                             Picture2=Picture2,Picture3=Picture3,Picture4=Picture5,Picture6=Picture6,
                                             Picture7=Picture7,Picture8=Picture8,Picture9=Picture9))
        else:
            result = json.dumps({'state': 0, 'msg': '请登录'})
        response = HttpResponse(result, content_type="application/json")
        response["Access-Control-Allow-Origin"] = "*"
    except Exception as e:
        print(e)
        response = HttpResponse('服务器异常')
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
    except Exception as e:
        print(e)
        response = HttpResponse('服务器异常')
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