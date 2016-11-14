"""HeZu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from HeZe.view.userviews import login, sendmessage, reg, logout, revisepsw, revisephoto, resetpsw, locate
from HeZe.view.hezuview import hezuinfors, sendhezu, selectinfors
from HeZe.view.imview import gettoken,getfriends,attention
from HeZe.view.circleview import sendcircle, circleinfo, circleoneinfo, sendcomment, commentinfo
from HeZe.view.testview import f

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('login/', login),
    url('logout/', logout),
    url('sendmessage/', sendmessage),
    url('reg/', reg),
    url('hezuinfors/', hezuinfors),
    url('sendhezu', sendhezu),
    url('revisepsw', revisepsw),
    url('revisephoto', revisephoto),
    url('resetpsw', resetpsw),
    url('gettoken', gettoken),
    url('getfriends', getfriends),
    url('attention', attention),
    url('sendcircle', sendcircle),
    url('circleinfo', circleinfo),
    url('circleoneinfo', circleoneinfo),
    url('sendcomment', sendcomment),
    url('commentinfo', commentinfo),
    url('selecthezuinfors', selectinfors),
    url('locate', locate),
    url('test', f),
]
