import xadmin
from .models import UserRecord


class UserRecordXadmin(object):
    # 显示内容
    list_display = ['user', 'start_time', 'end_time', 'month', 'type', 'data_id', 'data_detail']
    # 搜索字段
    search_fields = ['type', 'user', 'month']
    # 筛选字段
    list_filter = ['type', 'user', 'month']


xadmin.site.register(UserRecord, UserRecordXadmin)
