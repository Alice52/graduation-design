import xadmin
from .models import UserAsk, UserLove, UserCourse, UserComment, UserMessage


class UserAskXadmin(object):
    # 显示内容
    list_display = ['name', 'phone', 'course', 'add_time']
    # 搜索字段
    search_fields = ['name', 'phone', 'course']
    # 筛选字段
    list_filter = ['name', 'phone', 'course', 'add_time']


class UserLoveXadmin(object):
    # 显示内容
    list_display = ['love_id', 'love_type', 'love_status', 'love_man', 'add_time']
    # 搜索字段
    search_fields = ['love_id', 'love_type', 'love_status', 'love_man']
    # 筛选字段
    list_filter = ['love_id', 'love_type', 'love_status', 'love_man', 'add_time']


class UserCourseXadmin(object):
    # 显示内容
    list_display = ['study_man', 'study_course', 'add_time']
    # 搜索字段
    search_fields = ['study_man', 'study_course']
    # 筛选字段
    list_filter = ['study_man', 'study_course', 'add_time']


class UserCommentXadmin(object):
    # 显示内容
    list_display = ['comment_content', 'comment_man', 'comment_course', 'add_time']
    # 搜索字段
    search_fields = ['comment_content', 'comment_man', 'comment_course']
    # 筛选字段
    list_filter = ['comment_content', 'comment_man', 'comment_course', 'add_time']


class UserMessageXadmin(object):
    # 显示内容
    list_display = ['message_man', 'message_content', 'message_status', 'add_time']
    # 搜索字段
    search_fields = ['message_man', 'message_content', 'message_status']
    # 筛选字段
    list_filter = ['message_man', 'message_content', 'message_status', 'add_time']


xadmin.site.register(UserAsk, UserAskXadmin)
xadmin.site.register(UserLove, UserLoveXadmin)
xadmin.site.register(UserCourse, UserCourseXadmin)
xadmin.site.register(UserComment, UserCommentXadmin)
xadmin.site.register(UserMessage, UserMessageXadmin)
