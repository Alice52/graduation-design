from django.shortcuts import render, redirect, reverse, HttpResponse

from .froms import UserRegisterForm, UserLoginForm, UserForgetForm, UserResetForm
from .models import UserProfile, EmailVerifyCode
from django.db.models import Q
from utils.sendEmail import send_email_code
from django.contrib.auth import authenticate, logout, login


# Create your views here.
def index(request):
    return render(request, 'index.html')


def user_register(request):
    if request.method == 'GET':
        user_register_form = UserRegisterForm()
        return render(request, 'register.html', {
            'user_register_form': user_register_form
        })
    else:
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            email = user_register_form.cleaned_data['email']
            password = user_register_form.cleaned_data['password']

            user_list = UserProfile.objects.filter(Q(username=email) | Q(email=email))
            if user_list:
                return render(request, 'register.html', {
                    'msg': '用户已经注册'
                })
            else:
                user = UserProfile()
                user.username = email
                user.set_password(password)
                user.email = email
                user.save()
                # send email
                send_email_code(email, 1)
                return render(request, 'register.html', {
                    'msg': '请去邮箱激活账号'
                })
        else:
            return render(request, 'register.html', {
                'user_register_form': user_register_form
            })


def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user_login_from = UserLoginForm(request.POST)
        if user_login_from.is_valid():
            email = user_login_from.cleaned_data['email']
            password = user_login_from.cleaned_data['password']

            user = authenticate(username=email, password=password)
            if user:
                if user.is_start:
                    login(request, user)
                    return redirect(reverse('index'))
                else:
                    return render(request, 'login.html', {
                        'msg': '请去邮箱激活账号'
                    })
            else:
                return render(request, 'login.html', {
                    'msg': '邮箱或密码不对'
                })
        else:
            return render(request, 'login.html', {
                'user_login_from': user_login_from
            })


def user_logout(request):
    logout(request)
    return redirect(reverse('index'))


def user_active(request, code):
    if code:
        email_ver_list = EmailVerifyCode.objects.filter(code=code)
        if email_ver_list:
            email_ver = email_ver_list[0]
            email = email_ver.email
            user_list = UserProfile.objects.filter(email=email)
            if user_list:
                user = user_list[0]
                user.is_start = True
                user.save()
                return redirect(reverse('users:user_login'))
            else:
                pass
        else:
            pass
    else:
        pass


def user_forget(request):
    if request.method == 'GET':
        user_forget_from = UserForgetForm()
        return render(request, 'forgetpwd.html', {
            'user_forget_from': user_forget_from
        })
    else:
        user_forget_from = UserForgetForm(request.POST)
        if user_forget_from.is_valid():
            email = user_forget_from.cleaned_data['email']
            user_list = UserProfile.objects.filter(email=email)
            if user_list:
                user = user_list[0]
                send_email_code(email, 2)
                return render(request, 'forgetpwd.html', {
                    'msg': '请尽快区邮箱重置密码'
                })
            else:
                return render(request, 'forgetpwd.html', {
                    'msg': '用户不存在'
                })
        else:
            return render(request, 'forgetpwd.html', {
                'user_forget_from': user_forget_from
            })


def user_reset(request, code):
    if code:
        if request.method == 'GET':
            return render(request, 'password_reset.html', {
                'code': code
            })
        else:
            user_reset_from = UserResetForm(request.POST)
            if user_reset_from.is_valid():
                password = user_reset_from.cleaned_data['password']
                password1 = user_reset_from.cleaned_data['password1']
                if password == password1:
                    email_ver_list = EmailVerifyCode.objects.filter(code=code)
                    if email_ver_list:
                        email = email_ver_list[0].email
                        if email:
                            user_list = UserProfile.objects.filter(email=email)
                            if user_list:
                                user = user_list[0]
                                user.set_password(password)
                                user.save()
                                return redirect(reverse('users:user_login'))
                            else:
                                return render(request, 'password_reset.html', {
                                    'msg': '用户不存在',
                                    'code': code
                                })
                        else:
                            return render(request, 'password_reset.html', {
                                'msg': '用户不存在',
                                'code': code
                            })
                    else:
                        return render(request, 'password_reset.html', {
                            'msg': '用户不存在',
                            'code': code
                        })
                else:
                    return render(request, 'password_reset.html', {
                        'msg': '两次输入的密码不同',
                        'code': code
                    })
            else:
                return render(request, 'password_reset.html', {
                    'user_reset_from': user_reset_from,
                    'code': code
                })
