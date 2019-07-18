from django.shortcuts import render, reverse
from LoginApp.models import LoginUser
from django.http import HttpResponseRedirect, JsonResponse
import hashlib
from django.contrib.auth.hashers import check_password
from datetime import timedelta

"""
拓展功能：
    1、密码加密
        注册加密
        登陆需要加密
    2、cookie校验编写装饰器
    3、cookie和session进行混合校验
    4、用户名重复不可以注册
        1、后端校验
        2、ajax前端校验
"""


# def is_login(func):
#     def check(request):
#         try:
#             request.session['user_id']
#         except:
#             return HttpResponseRedirect(reverse('users:login'))
#         return func(request)
#
#     return check


def is_user_exist(username):
    """检验用户是否存在"""
    return LoginUser.objects.filter(username=username).first()


# 装饰器
def is_login(func):
    """进行登录校验"""

    def check(request, *args, **kwargs):
        username = request.COOKIES.get("username")
        session_user = request.session.get("username")
        if username and session_user:
            user = is_user_exist(username)
            if user and username == session_user:
                return func(request, *args, **kwargs)
        return HttpResponseRedirect('/login/login/')

    return check


def md5_encrypt(text):
    """md5加密"""
    m5 = hashlib.md5()
    text = text.encode(encoding='utf-8')
    m5.update(text)
    return m5.hexdigest()


@is_login
def index(request):
    return render(request, 'loginapp/index.html')


def register(request):
    result = {"content": ""}
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password and not is_user_exist(username):
            user = LoginUser()
            user.username = username
            user.password = md5_encrypt(password)
            user.save()
            return HttpResponseRedirect('/login/login/')
        else:
            result["content"] = "用户名或者密码不可以为空"
    return render(request, 'loginapp/register.html', locals())


def login(request):
    result = {"content": ""}
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user = is_user_exist(username)
            if user:
                if not check_password(password, user.password):
                    result["content"] = "密码错误"
                else:
                    response = HttpResponseRedirect("/login/index/")
                    response.set_cookie("username", user.username)
                    request.session["username"] = user.username  # 设置session
                    request.session.set_expiry(timedelta(days=1))
                    return response

                if md5_encrypt(password) == user.password:
                    response = HttpResponseRedirect("/login/index/")
                    response.set_cookie("username", user.username)
                    request.session["username"] = user.username  # 设置session
                    return response
                else:
                    result["content"] = "密码错误"
            else:
                result["content"] = "用户名不存在"
        else:
            result["content"] = "用户名或者密码不可以为空"

    return render(request, "loginapp/login.html", locals())


def logout(request):
    response = HttpResponseRedirect('/login/login/')
    response.delete_cookie("username")
    return response


def ajax_user_valid(request):
    """ajax检验用户名是否存在"""
    result = {"status": "error", "content": ""}
    username = request.GET.get("username")
    if username:
        user = is_user_exist(username)
        if user:
            result["content"] = "用户名已存在"
        else:
            result["content"] = "用户名可以使用"
            result["status"] = "success"
    else:
        result["content"] = "用户名不可以为空"
    return JsonResponse(result)


def temp_filter(request):
    test_data = [
        {"name": "张三", "birthday": "2009-02-06"},
        {"name": "李四", "birthday": "1999年2月16日"},
        {"name": "王五", "birthday": "1989/12/6"},
        {"name": "赵六", "birthday": "1979.10.06"},
        {"name": "锅巴", "birthday": "1969,5,6"},
    ]

    return render(request, 'loginapp/temp_filter.html', locals())
