from django.http import HttpResponse
from HeZe.controller.userservice.login import dologin
from HeZe.controller.userservice.islog import islog
from HeZe.controller.userservice.register import registe
import json


#发合租
def sendhezu(request):
    UserPhone = request.GET.get('UserPhone')
    SecretKey = request.GET.get('SecretKey')
    Information = request.GET.get('Information')
    Address = request.GET.get('Address')
    Number = request.GET.get('Number')
#end