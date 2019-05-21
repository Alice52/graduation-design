import xadmin
from .models import UserLove, UserCourse, UserComment


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



xadmin.site.register(UserLove, UserLoveXadmin)
xadmin.site.register(UserCourse, UserCourseXadmin)
xadmin.site.register(UserComment, UserCommentXadmin)
