from datetime import datetime
from django.core.cache import cache
from zcEducation import settings
from .models import UserRecord
from django.utils.deprecation import MiddlewareMixin
import re


class OnlineStatusMiddleware(MiddlewareMixin):

    # def process_request(self, request):
    #     if request.user.is_authenticated():
    #         cache_key = '%s_last_login' % request.user.username
    #         now = datetime.now()
    #         userrecord = UserRecord.objects.filter(user=request.user).order_by('-start_time')
    #         # 用户是第一次登录、或者是缓存过去、或者是服务器重启导致缓存消失
    #         if not cache.get(cache_key):
    #             print('#### cache not found #####')
    #             if not userrecord:
    #                 ur = UserRecord()
    #                 ur.user = request.user
    #                 ur.month = now.month
    #                 ur.start_time = now
    #                 ur.save()
    #             else:
    #                 ur = userrecord[0]
    #                 if ur.end_time:
    #                     ur = UserRecord()
    #                     ur.user = request.user
    #                     ur.month = now.month
    #                     ur.start_time = now
    #                     ur.save()
    #                 else:
    #                     ur.end_time = now
    #                     ur.save()
    #
    #             cache.set(cache_key, now, settings.USER_LAST_LOGIN_EXPIRE)
    #
    #         else:
    #             print("##### cache found ######")
    #             if 'user_logout' in request.path:
    #                 ur = userrecord[0]
    #                 if not ur.end_time:
    #                     ur.end_time = now
    #                     ur.save()
    #             if 'get_user' in request.path:
    #                 ur = UserRecord()
    #                 ur.user = request.user
    #                 ur.month = now.month
    #                 ur.start_time = now
    #                 ur.save()
    #             cache.set(cache_key, now, settings.USER_LAST_LOGIN_EXPIRE)
    def process_request(self, request):
        cache_key = 'userinfo_'+request.user.username
        cache_request_path_key = "request_path" + request.user.username
        user_expire = cache.ttl(cache_key)
        islogin = False
        if not user_expire:
            if request.user.is_authenticated():
                islogin = True
        elif user_expire >= 5 * 60:
            islogin = True
        # if request.user.is_authenticated():  # 验证 session 是否过期
        # if user_expire >= 5 * 60:  # 验证 session 是否过期
        if islogin:
            now = datetime.now()
            lastPath = cache.get(cache_request_path_key)
            this_path = request.path  # 将上一次的 path 缓存到 redis
            if 'get_user' in this_path:
                cache.expire(cache_request_path_key, settings.REDIS_TIMEOUT)
            else:
                cache.set(cache_request_path_key, this_path, settings.REDIS_TIMEOUT)

            this_user = request.user
            # 缓存整个 user 的信息
            userinfo = cache.get(cache_key)
            if not userinfo:
                # cache.set(cache_key, json.dumps(user_name), settings.NEVER_REDIS_TIMEOUT)
                cache.set(cache_key, request.user, settings.REDIS_TIMEOUT)
            else:
                cache.expire(cache_key, settings.REDIS_TIMEOUT)

            # 记录 login/logout
            userrecord = UserRecord.objects.filter(user=request.user, type=1).order_by('-start_time')
            if not userrecord:
                ur = UserRecord()
                ur.user = request.user
                ur.month = now.month
                ur.start_time = now
                ur.save()
            elif 'get_user' in request.path:  # F5
                ur = userrecord[0]
                if not ur.end_time:
                    pass
                else:
                    ur = UserRecord()
                    ur.user = request.user
                    ur.month = now.month
                    ur.start_time = now
                    ur.save()
            elif 'user_logout' in request.path:  # 长时间无操作 默认退出
                # 清除 redis 中的这个 user 的信息:  last_path,
                cache.delete_pattern(cache_key)
                cache.delete_pattern(cache_request_path_key)
                # cache.get()
                ur = userrecord[0]
                ur.end_time = now
                ur.save()

            # 记录用户所有的点击行为
            if not lastPath or lastPath != this_path:
                if 'list' in this_path:
                    last_record_s = UserRecord.objects.filter(user=request.user, end_time=None).order_by('-start_time')
                    if last_record_s.count() > 1:
                        record = last_record_s[0]
                        record.end_time = now
                        record.save()
                elif 'user_logout' in request.path or 'user' in request.path or 'operations' in this_path or 'course_chapter' in this_path:
                    pass
                else:
                    click_record = UserRecord()  # 过滤掉 F5 的问题
                    last_record_s = UserRecord.objects.filter(user=request.user, end_time=None).order_by('-start_time')
                    if last_record_s.count() == 1:  # lastPath == null
                        data_id = re.findall('/\d+', this_path)
                        if 'media/vedio' in this_path:  # 如果发送了请求, 则表示这个视屏播放结束(默认)
                            data_detail = re.findall(r'(?<=media/vedio/).*(?=)', this_path)
                            data_detail = data_detail[len(data_detail)-1][:-4]
                            click_record.data_detail = data_detail
                            click_record.user = this_user
                            click_record.start_time = now
                            click_record.month = now.month
                            click_record.type = 5
                            click_record.save()
                        elif data_id:
                            data_id = data_id[len(data_id)-1][1:]
                            click_record.user = this_user
                            click_record.start_time = now
                            click_record.month = now.month
                            click_record.data_id = data_id
                            # data_detail = re.findall(r'(?<=(\w)/)(\w+).*(?=/)', this_path)
                            if 'teacher'in this_path:
                                click_record.data_detail = this_path
                                click_record.type = 4
                                click_record.save()
                            elif 'org_' in this_path:
                                click_record.data_detail = this_path
                                click_record.type = 3
                                click_record.save()
                            elif 'course' in this_path:
                                click_record.data_detail = this_path
                                click_record.type = 2
                                click_record.save()
                            else:
                                click_record.save()
                        if not data_id:
                            pass
                    elif last_record_s.count() > 1:
                        last_record = last_record_s[0]
                        last_record.end_time = now
                        last_record.save()
                    # elif last_record_s.count() == 1:
                        # reg 匹配 path 中的 id
                        data_id = re.findall('/\d+', this_path)
                        if 'media/vedio' in this_path:  # 如果发送了请求, 则表示这个视屏播放结束(默认)
                            data_detail = re.findall(r'(?<=media/vedio/).*(?=)', this_path)
                            data_detail = data_detail[len(data_detail)-1][:-4]
                            click_record.data_detail = data_detail
                            click_record.user = this_user
                            click_record.start_time = now
                            click_record.month = now.month
                            click_record.type = 5
                            click_record.save()
                        elif data_id:
                            data_id = data_id[len(data_id)-1][1:]
                            click_record.user = this_user
                            click_record.start_time = now
                            click_record.month = now.month
                            click_record.data_id = data_id
                            if 'teacher'in this_path:
                                click_record.data_detail = this_path
                                click_record.type = 4
                                click_record.save()
                            elif 'org_' in this_path:
                                click_record.data_detail = this_path
                                click_record.type = 3
                                click_record.save()
                            elif 'course' in this_path:
                                click_record.data_detail = this_path
                                click_record.type = 2
                                click_record.save()
                            else:
                                pass
                        if not data_id:
                            pass
                    else:
                        pass
            elif lastPath == this_path:
                cache.expire(cache_request_path_key, settings.REDIS_TIMEOUT)
            else:
                pass

        return None
