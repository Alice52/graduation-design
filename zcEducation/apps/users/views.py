from django.shortcuts import render, redirect, reverse, HttpResponse
from .forms import UserRegisterForm, UserLoginForm, UserForgetForm, UserResetForm, \
    UserChangeEmailForm, UserChangeInfoForm, UserResetEmailForm, UserChangeImageForm
from .models import UserProfile, EmailVerifyCode, BannerInfo
from django.db.models import Q
from django.contrib.auth import authenticate, logout, login
from utils.sendEmail import send_email_code
from django.http import JsonResponse
from django.core import serializers
from datetime import datetime
from operations.models import UserLove
from orgs.models import OrgInfo, TeacherInfo
from courses.models import CourseInfo
from django.views.decorators.csrf import csrf_exempt
from .jobs import job_session_invalid, job_send_sumary_email
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from zcEducation import settings
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job


@cache_page(60 * 24 * 60)
def index(request):
    all_banners = serializers.serialize("json", BannerInfo.objects.all().order_by('-add_time')[:5])
    banner_courses = serializers.serialize("json", CourseInfo.objects.filter(is_banner=True)[:3])
    all_courses = serializers.serialize("json", CourseInfo.objects.filter(is_banner=False)[:6])
    all_orgs = serializers.serialize("json", OrgInfo.objects.all()[:15])

    return JsonResponse({
        'all_banners': all_banners,
        'banner_courses': banner_courses,
        'all_courses': all_courses,
        'all_orgs': all_orgs
    })


def get_user(request):
    user = None
    u = UserProfile.objects.filter(username=request.user.username)
    if u.count() > 0:
        user = serializers.serialize("json", u),

    return JsonResponse({
        'user': user,
    })


def user_register(request):
    user_register_form = UserRegisterForm(request.POST)
    if user_register_form.is_valid():
        email = user_register_form.cleaned_data['email']
        password = user_register_form.cleaned_data['password']

        user_list = UserProfile.objects.filter(Q(username=email) | Q(email=email))
        if user_list:
            return JsonResponse({
                'errMsg': '用户已经存在'
            })
        else:
            a = UserProfile()
            a.username = email
            a.set_password(password)
            a.email = email
            a.image = 'user/default.jpg'
            a.save()
            send_email_code(email, 1)
            return JsonResponse({
                'errMsg': '请去邮箱激活账号'
            })
    else:
        return JsonResponse({
            'errMsg': '输入信息格式错误'
        })


@csrf_exempt
def user_login(request):
    user_login_form = UserLoginForm(request.POST)
    if user_login_form.is_valid():
        username = user_login_form.cleaned_data['username']
        password = user_login_form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_start:
                login(request, user)
                url = request.COOKIES.get('url', '/')
                return JsonResponse({
                    'errMsg': 'ok',
                    'url': url
                })
            else:
                return JsonResponse({
                    'errMsg': '请去邮箱激活账号'
                })
        else:
            return JsonResponse({
                'errMsg': '邮箱或密码不对'
            })
    else:
        return JsonResponse({
            'errMsg': '请出入正确格式的邮箱'
        })


def user_logout(request):
    logout(request)

    return JsonResponse({
        'errMsg': 'ok',
        'url': '/'
    })


def user_active(request, code):
    if code:
        email_ver_list = EmailVerifyCode.objects.filter(code=code)
        if email_ver_list:
            email_ver = email_ver_list[0]
            email = email_ver.email
            user_list = UserProfile.objects.filter(username=email)
            if user_list:
                user = user_list[0]
                user.is_start = True
                user.save()
                return JsonResponse({
                    'errMsg': 'ok'
                })
            else:
                pass
        else:
            pass
    else:
        pass


def user_forget(request):
    user_forget_form = UserForgetForm(request.POST)
    if user_forget_form.is_valid():
        email = user_forget_form.cleaned_data['email']
        user_list = UserProfile.objects.filter(email=email)
        if user_list:
            user = user_list[0]
            send_email_code(email, 2)
            return JsonResponse({
                'errMsg': '请尽快区邮箱重置密码'
            })
        else:
            return JsonResponse({
                'errMsg': '用户不存在'
            })
    else:
        return JsonResponse({
            'errMsg': '邮箱格式不正确'
        })


def user_reset(request, code):
    if code:
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
                            return JsonResponse({
                                'errMsg': 'ok'
                            })
                        else:
                            return JsonResponse({
                                'msg': '用户不存在',
                            })
                    else:
                        return JsonResponse({
                            'msg': '用户不存在',
                        })
                else:
                    return JsonResponse({
                        'msg': '用户不存在',
                    })
            else:
                return JsonResponse({
                    'msg': '两次输入的密码不同',
                })
        else:
            return JsonResponse({
                'errMsg': '请输入3到16位的密码',
            })


def user_info(request):
    user = None
    u = UserProfile.objects.filter(username=request.user.username)
    if u.count() > 0:
        user = serializers.serialize("json", u),
    return JsonResponse({
        'user': user
    })


# def user_changeimage(request):
#     iamge = 'user/' + str(request.FILES.get('image'))
#     com = re.compile('^.*(\.gif|\.jpeg|\.png|\.jpg|\.bmp)$')
#     if com.match(iamge):
#         user = UserProfile.objects.filter(id=request.user.id)[0]
#         user.image = iamge
#         # upload image  MEDIA_URL
#         filename = BASE_DIR + os.path.join(MEDIA_URL, iamge)
#         fobj = open(filename, 'wb');
#         for chrunk in request.FILES.get('image').chunks():
#             fobj.write(chrunk);
#         fobj.close();
#         user.save()
#         return JsonResponse({'status': 'ok'})
#     else:
#         return JsonResponse({'status': 'fail'})
def user_changeimage(request):
    # instance  指明实例是什么，做修改的时候，我们需要知道是给哪个对象实例进行修改
    # 如果不指明，那么就会被当作创建对象去执行，而我们只有一个图片，就一定会报错。
    conct = request.POST
    user_changeimage_form = UserChangeImageForm(request.POST, request.FILES, instance=request.user)
    if user_changeimage_form.is_valid():
        user_changeimage_form.save(commit=True)
        u = UserProfile.objects.filter(id=request.user.id)
        cache_key = 'userinfo_'+request.user.username
        cache.set(cache_key, u, settings.REDIS_TIMEOUT)
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'fail'})


def user_changeinfo(request):
    user_changeinfo_form = UserChangeInfoForm(request.POST, instance=request.user)
    if user_changeinfo_form.is_valid():
        user_changeinfo_form.save(commit=True)
        u = UserProfile.objects.filter(id=request.user.id)
        cache_key = 'userinfo_'+request.user.username
        cache.set(cache_key, u, settings.REDIS_TIMEOUT)
        return JsonResponse({"status": 'ok', 'msg': '修改成功'})
    else:
        return JsonResponse({"status": 'fail', 'msg': '修改失败'})


def user_changeemail(request):
    '''
    当用户修改邮箱，点击获取验证码的时候，会通过这个函数处理，发送邮箱验证码
    :param request: http请求对象
    :return: 返回json数据，在模板页面当中去处理
    '''
    user_changeemail_form = UserChangeEmailForm(request.POST)
    if user_changeemail_form.is_valid():
        email = user_changeemail_form.cleaned_data['email']
        user_list = UserProfile.objects.filter(Q(email=email) | Q(username=email))
        if user_list:
            return JsonResponse({'status': 'fail', 'msg': '邮箱已经被绑定'})
        else:
            # 我们在发送邮箱验证码之前，应该去邮箱验证码的表当中去查找，看之前有没有往当前这个邮箱发送过修改邮箱这个类型的验证码
            email_ver_list = EmailVerifyCode.objects.filter(email=email, send_type=3)
            # 如果发送过验证码，那么我们就拿到最近发送的这一个
            if email_ver_list:
                email_ver = email_ver_list.order_by('-add_time')[0]
                # 判断当前时间和最近发送的验证码添加时间之差
                if (datetime.now() - email_ver.add_time).seconds > 60:
                    # 如果我们重新发送了新的验证码，那么以前最近发的就被清了
                    send_email_code(email, 3)
                    email_ver.delete()
                    return JsonResponse({'status': 'ok', 'msg': '请尽快去邮箱当中获取验证码'})
                else:
                    return JsonResponse({'status': 'fail', 'msg': '请不要重复发送验证码，1分钟后重试'})
            else:
                send_email_code(email, 3)
                return JsonResponse({'status': 'ok', 'msg': '请尽快去邮箱当中获取验证码'})
    else:
        return JsonResponse({'status': 'fail', 'msg': '您的邮箱有问题'})


# def user_resetemail(request):
#     user_resetemail_form = UserResetEmailForm(request.POST)
#     if user_resetemail_form.is_valid():
#         email = user_resetemail_form.cleaned_data['email']
#         code = user_resetemail_form.cleaned_data['code']
#         email_ver_list = EmailVerifyCode.objects.filter(email=email, code=code)
#         if email_ver_list:
#             email_ver = email_ver_list[0]
#             if (datetime.now() - email_ver.add_time).seconds < 60:
#                 request.user.username = email
#                 request.user.email = email
#                 request.user.save()
#                 return JsonResponse({'status': 'ok', 'msg': '邮箱修改成功'})
#             else:
#                 return JsonResponse({'status': 'fail', 'msg': '验证码失效，请重新发送验证码'})
#         else:
#             return JsonResponse({'status': 'fail', 'msg': '邮箱或者验证码有误'})
#     else:
#         return JsonResponse({'status': 'fail', 'msg': '邮箱或者验证码不合法'})


def user_course(request):
    usercourse_list = request.user.usercourse_set.all()
    course_list = serializers.serialize("json", [usercourse.study_course for usercourse in usercourse_list])
    return JsonResponse({
        'course_list': course_list
    })


def user_loveorg(request):
    userloveorg_list = UserLove.objects.filter(love_man=request.user, love_type=1, love_status=True)
    org_ids = [userloveorg.love_id for userloveorg in userloveorg_list]
    org_list = serializers.serialize("json", OrgInfo.objects.filter(id__in=org_ids))

    return JsonResponse({
        'org_list': org_list
    })


# rewrite
def user_loveteacher(request):
    userloveteacher_list = UserLove.objects.filter(love_man=request.user, love_type=3, love_status=True)
    teacher_ids = [userloveteacher.love_id for userloveteacher in userloveteacher_list]
    teacher_list = serializers.serialize("json", TeacherInfo.objects.filter(id__in=teacher_ids))

    return JsonResponse({
        'teacher_list': teacher_list
    })


def user_lovecourse(request):
    userlovecourse_list = UserLove.objects.filter(love_man=request.user, love_type=2, love_status=True)
    course_ids = [userlovecourse.love_id for userlovecourse in userlovecourse_list]
    course_list = serializers.serialize("json", CourseInfo.objects.filter(id__in=course_ids))

    return JsonResponse({
        'course_list': course_list
    })

try:
    # 实例化调度器
    scheduler = BackgroundScheduler()
    # 调度器使用DjangoJobStore()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # 设置定时任务，选择方式为interval，时间间隔为10s
    # 另一种方式为每天固定时间执行任务，对应代码为：
    # @register_job(scheduler, 'cron', day_of_week='mon-fri', hour='9', minute='30', second='10',id='task_time')
    @register_job(scheduler, "interval", seconds=5 * 60,  replace_existing=True, misfire_grace_time=4 * 60)
    def my_job():
        # 这里写你要执行的任务
        print("dsaddasdsa")
        job_session_invalid()

    @register_job(scheduler, "cron", month='1-12', day='1', hour='7',  replace_existing=True, misfire_grace_time=4 * 60 * 60)
    def emial_job():
        # 这里写你要执行的任务
        job_send_sumary_email()

    register_events(scheduler)
    scheduler.start()
except Exception as e:
    print(e)
    pass
    # 有错误就停止定时器
    # scheduler.shutdown()

# from apscheduler.schedulers.blocking import BlockingScheduler
# import datetime
# from apscheduler.jobstores.memory import MemoryJobStore
# from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
#
#
# def my_job(id='my_job'):
#     print('sdsdsadsd_job')
#     # job_session_invalid()
#
#
# jobstores = {
#     'default': MemoryJobStore()
#
# }
# executors = {
#     'default': ThreadPoolExecutor(20),
#     'processpool': ProcessPoolExecutor(10)
# }
# job_defaults = {
#     'coalesce': False,
#     'max_instances': 3
# }
# scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)
# scheduler.add_job(my_job, args=['job_interval', ], id='job_interval', trigger='interval', seconds=50, replace_existing=True)
# try:
#     scheduler.start()
# except SystemExit:
#     print('exit')
#     exit()
