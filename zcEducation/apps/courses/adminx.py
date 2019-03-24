import xadmin
from .models import CourseInfo, LessonInfo, VideoInfo, SourceInfo


class CourseInfoXadmin(object):
    # 显示内容
    list_display = ['image', 'name', 'study_time', 'level', 'desc', 'category', 'add_time', 'orginfo',
                    'teacherinfo']
    # 搜索字段
    search_fields = ['image', 'name', 'study_time', 'level', 'desc', 'category', 'add_time', 'orginfo',
                     'teacherinfo']
    # 筛选字段
    list_filter = ['image', 'name', 'study_time', 'level', 'desc', 'category', 'add_time', 'orginfo',
                   'teacherinfo']


class LessonInfoXadmin(object):
    # 显示内容
    list_display = ['name', 'courseinfo', 'add_time']
    # 搜索字段
    search_fields = ['name', 'courseinfo']
    # 筛选字段
    list_filter = ['name', 'courseinfo', 'add_time']


class VideoInfoXadmin(object):
    # 显示内容
    list_display = ['name', 'study_time', 'url', 'add_time', 'lessoninfo']
    # 搜索字段
    search_fields = ['name', 'study_time', 'url', 'lessoninfo']
    # 筛选字段
    list_filter = ['name', 'study_time', 'url', 'add_time', 'lessoninfo']


class SourceInfoXadmin(object):
    # 显示内容
    list_display = ['name', 'down_load', 'courseinfo', 'add_time']
    # 搜索字段
    search_fields = ['name', 'down_load', 'courseinfo']
    # 筛选字段
    list_filter = ['name', 'down_load', 'courseinfo', 'add_time']


xadmin.site.register(CourseInfo, CourseInfoXadmin)
xadmin.site.register(LessonInfo, LessonInfoXadmin)
xadmin.site.register(VideoInfo, VideoInfoXadmin)
xadmin.site.register(SourceInfo, SourceInfoXadmin)
