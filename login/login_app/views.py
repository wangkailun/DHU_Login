from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random
import io
from .models import User
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "login_app/login.html")


def register(request):
    return render(request, "login_app/register.html")


def check_user(request):
    request.encoding = "utf-8"
    if "userName" in request.Get and "passWord" in request.Get and request.GET['userName'] and request.GET['passWord']:
        userName = request.GET['userName']
        passWord = request.GET['passWord']
        user = User.objects.filter(name=userName)
        # 如果列表不为空
        if user:
            if user.pwd == passWord:
                return HttpResponse("<p>登录成功</p>")
            else:
                return HttpResponse("<p>密码不正确</p>")
        else:
            return HttpResponse("<p>用户名不存在</p>")
    else:
        return HttpResponse("<p>用户名或者密码不能为空</p>")


@csrf_exempt
def add_user(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = User(name=username, pwd=password)
    user.save()
    return HttpResponse("<p>hello world</p>")
