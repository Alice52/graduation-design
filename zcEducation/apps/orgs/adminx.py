import xadmin
from .models import TeacherInfo, CityInfo, OrgsInfo


class CityInfoXadmin(object):
    # 显示内容
    list_display = ['name', 'add_time']
    # 搜索字段
    search_fields = ['name']
    # 筛选字段
    list_filter = ['name', 'add_time']


class OrgsInfoXadmin(object):
    list_display = ['image', 'name', 'course_num', 'study_num', 'address', 'desc', 'detail', 'love_num', 'click_num',
                    'category', 'cityinfo', 'add_time']
    search_fields = ['image', 'name', 'course_num', 'study_num', 'address', 'desc', 'detail', 'love_num', 'click_num',
                     'category', 'cityinfo']
    list_filter = ['image', 'name', 'course_num', 'study_num', 'address', 'desc', 'detail', 'love_num', 'click_num',
                   'category', 'cityinfo', 'add_time']


class TeacherInfoXadmin(object):
    list_display = ['image', 'name', 'work_year', 'work_position', 'work_style', 'age', 'gender', 'love_num',
                    'click_num', 'work_company', 'add_time']
    search_fields = ['image', 'name', 'work_year', 'work_position', 'work_style', 'age', 'gender', 'love_num',
                     'click_num', 'work_company']
    list_filter = ['image', 'name', 'work_year', 'work_position', 'work_style', 'age', 'gender', 'love_num',
                   'click_num', 'work_company', 'add_time']


xadmin.site.register(TeacherInfo, TeacherInfoXadmin)
xadmin.site.register(CityInfo, CityInfoXadmin)
xadmin.site.register(OrgsInfo, OrgsInfoXadmin)
