from online_status.models import UserRecord
from django.core.cache import cache
from datetime import datetime
from .models import UserProfile
from utils.sendEmail import send_email_code_job, send_email_code


def job_session_invalid():
    print("session_job")
    # userrecord = UserRecord.objects.filter(user=request.user).order_by('-start_time')
    # cache.keys()
    all_cache_key_in_cache = cache.iter_keys("userinfo_*")
    for cache_key in all_cache_key_in_cache:
        expire_time = cache.ttl(cache_key)
        if expire_time < 60 * 4 + 58:
        # if expire_time < 60:
            userinfo = cache.get(cache_key)
            userrecord = UserRecord.objects.filter(user=userinfo, end_time=None).order_by('-start_time')
            cache.delete_pattern(cache_key)
            cache_request_path_key = "request_path" + userinfo.username
            cache.delete_pattern(cache_request_path_key)
            for record in userrecord:
                record.end_time = datetime.now()
                record.save()
            # if not userrecord.end_time:
            else:
                pass
        else:
            pass


def job_send_sumary_email():
    # 每个月月初发送给用户上个月的学习总结
    all_users = UserProfile.objects.all()
    email_month = datetime.now().month - 1
    try:
        for user in all_users:
            userrecored = UserRecord.objects.filter(month=email_month, user=user)
            if not userrecored:
                send_email_code(user.email, 3)
            else:
                learning_times = userrecored.filter(type=1).count()
                learning_courses_time = userrecored.filter(type=2)
                learning_time = 0
                for record in userrecored:
                    learning_time = learning_time+ (record.end_time-record.start_time).seconds
                send_email_code_job(user.email, learning_times, learning_courses_time, learning_time)
    except Exception as e:
        print('发送用户总结任务时出错' + e)
