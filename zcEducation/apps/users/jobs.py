from online_status.models import UserRecord
from django.core.cache import cache
from datetime import datetime


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
            userrecord = UserRecord.objects.filter(user=userinfo).order_by('-start_time')[0]
            if not userrecord.end_time:
                userrecord.end_time = datetime.now()
                userrecord.save()
            else:
                pass
        else:
            pass


def job_send_sumary_email():
    pass
