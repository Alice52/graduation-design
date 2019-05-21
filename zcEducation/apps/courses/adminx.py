import xadmin
from .models import *


# Create your models here.
class CourseInfoXadmin(object):
    list_display = ['image', 'name', 'study_num', 'level', 'love_num', 'category', 'orginfo', 'teacherinfo']
    search_fields = ['name', 'study_num', 'level', 'love_num', 'category']
    list_filter = ['name', 'study_num', 'level', 'love_num', 'category']

class LessonInfoXadmin(object):
    list_display = ['name', 'courseinfo', 'add_time']
    search_fields = ['name', 'courseinfo']
    list_filter = ['name', 'courseinfo']


class VideoInfoXadmin(object):
    list_display = ['name', 'study_time', 'url', 'lessoninfo']
    search_fields = ['name', 'study_time', 'lessoninfo']
    list_filter = ['name', 'study_time', 'lessoninfo']


class SourceInfoXadmin(object):
    list_display = ['name', 'down_load', 'courseinfo', 'add_time']
    search_fields = ['name', 'courseinfo']
    list_filter = ['name', 'courseinfo']


xadmin.site.register(CourseInfo, CourseInfoXadmin)
xadmin.site.register(LessonInfo, LessonInfoXadmin)
xadmin.site.register(VideoInfo, VideoInfoXadmin)
xadmin.site.register(SourceInfo, SourceInfoXadmin)
