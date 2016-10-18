from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from HeZe.controller.userservice.login import dologin
import json

# Create your views here.


def login(request):
    TelNumber = request.form.get('TelBumber')
    PassWord = request.form.get('PassWord')
    return HttpResponse(json.dumps(dologin(TelNumber, PassWord),content_type="application/json"))

