from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from HeZe.controller.userservice.login import dologin
import json

# Create your views here.


def login(request):
    UserPhone = request.POST.get('UserPhone')
    PassWord = request.POST.get('PassWord')
    return HttpResponse(dologin(UserPhone,PassWord)['msg'])

