# 1. setting.py 文件中的 INSTALLED_APPS 加入 xadmin:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'courses.apps.CoursesConfig',
    'orgs.apps.OrgsConfig',
    'operations.apps.OperationsConfig',
    'crispy_forms',
    'captcha',
    'DjangoUeditor',
    'online_status.apps.OnlineStatusConfig',
    'django_apscheduler',
    'xadmin',
]
# 2. 在本项目的 url.py 文件de urlpatterns 中添加 url(r'^xadmin/', xadmin.site.urls):
urlpatterns = [
    # include 分发
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^uedit/', include('DjangoUeditor.urls')),
    url(r'^users/', include(('users.urls', 'users'), namespace='users')),
    url(r'^orgs/', include(('orgs.urls', 'orgs'), namespace='orgs')),
    url(r'^operations/', include(('operations.urls', 'operations'), namespace='operations')),
    url(r'^courses/', include(('courses.urls', 'courses'), namespace='courses')),
    url(r'^$', index, name='index'),
]
# 3. 在控制台同步下数据库, 并创建用户
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser --username=zack --email=zzhang_xz@163.com
Password:
Password (again):
# 4. 创建不同模块的 xadmin.py 文件: 这里只是以用户操作做为示例, 其他模块一样.
import xadmin
from .models import *

class CityInfoXadmin(object):
    list_display = ['name', 'add_time']
    model_icon = 'fa fa-bath'

class OrgInfoXadmin(object):
    list_display = ['image', 'name', 'course_num', 'study_num', 'love_num', 'click_num', 'category', 'cityinfo']
    model_icon = 'fa fa-gift'
    style_fields = {'detail': 'ueditor'}

class TeacherInfoXadmin(object):
    list_display = ['image', 'name', 'work_year', 'work_position', 'click_num', 'age', 'gender', 'love_num']

xadmin.site.register(CityInfo, CityInfoXadmin)
xadmin.site.register(OrgInfo, OrgInfoXadmin)
xadmin.site.register(TeacherInfo, TeacherInfoXadmin)




# 用户
# 1. 配置 URL
urlpatterns = [
    url(r'^user_register/$', user_register, name='user_register'),
    url(r'^user_active/(\w+)/$', user_active, name='user_active'),
]
# 2. 注册账号
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

# 3. 激活账号
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


# usercourse
<div v-for="(course, index) in course_list" :key='index' :index='index' class="module1_5 box">
    <a @click="$router.push(`/courses/course_detail/${course.pk}`)" >
        <img width="214" height="190" class="scrollLoading" :src="getImgUrl(course.fields.image)">
    </a>
    <div class="des">
        <a @click="$router.push(`/courses/course_detail/${course.pk}`)" > <h2>{{course.fields.name}}</h2> </a>
        <span class="fl"> 课时： <i class="key">{{course.fields.study_time}}</i> </span>
        <span class="fr">学习人数：{{ course.fields.study_num }}</span>
    </div>
    <div class="bottom">
        <span class="browse fl" title="浏览次数">{{course.fields.click_num}}</span>
        <span class="star fr" title="收藏人数">{{course.fields.love_num}}</span>
    </div>
</div>

import axios from 'axios'
export default {
    data() {
        course_list:[],
        showComponent: false,
    },
    mounted() {
        axios({ url:'/api/users/user_course/', method: 'GET', }).then((response)=>{
        var res = response.data
        this.course_list = JSON.parse(res.course_list)
        this.showComponent = true
        }).catch((err)=> {
        console.log(err)
        })
    },
    methods:{
        getImgUrl: (bannerUrl) =>{ return "../../static/media/" + bannerUrl }
    },
};


# 课程
# 推荐
@login_decorator
@cache_page(60 * 24 * 60)
def course_video(request, course_id):
    if course_id:
        courseQuerySet = CourseInfo.objects.filter(id=int(course_id))
        course = courseQuerySet[0]

        usercourse_list = UserCourse.objects
                    .filter(study_man=request.user, study_course=course)
        if not usercourse_list:
            a = UserCourse()
            a.study_man = request.user
            a.save()
            course.study_num += 1
            course.save()

            # 维护机构的学习人数
            usercourse_list = UserCourse.objects
                    .filter(study_man=request.user).exclude(study_course=course)
            course_list = [usercourse.study_course for usercourse in usercourse_list]
            org_list = list(set([course1.orginfo for course1 in course_list]))
            if course.orginfo not in org_list:
                course.orginfo.study_num += 1
                course.orginfo.save()

        # 学过该课的同学还学过什么课程
        usercourse_list = UserCourse.objects.filter(study_course=course)
        user_list = [usercourse.study_man for usercourse in usercourse_list]
        usercourse_list = UserCourse.objects
                .filter(study_man__in=user_list).exclude(study_course=course)
        courseList = list(set([usercourse.study_course for usercourse in usercourse_list]))[:6]
        course_sources = SourceInfo.objects.filter(courseinfo=course)
        lesson_list = LessonInfo.objects.filter(courseinfo=course)
        lessons =[]
        for lesson in lesson_list:
            video_list = VideoInfo.objects.filter(lessoninfo=lesson)
            videos = []
            for video in video_list:
                a = {'name': video.name, 'url': str(video.url), 'study_time': video.study_time}
                videos.append(a)
            lessons.append({'name': lesson.name, 'video': videos})

        return JsonResponse({
            'course': serializers.serialize("json", courseQuerySet),
            'course_list': serializers.serialize("json", courseList),
            'course_sources': serializers.serialize("json", course_sources),
            'lesson_list': json.dumps(lessons),
            'status': 'login',
        })
# 用户评论
def course_comment(request, course_id):
    if course_id:
        courseQuerySet = CourseInfo.objects.filter(id=int(course_id))
        course = courseQuerySet[0]
        all_comments = course.usercomment_set.all().order_by('-add_time')[:10]
        comment_vo = []
        for comment in all_comments:
            user = UserProfile.objects.filter(id=comment.comment_man_id)[0]
            comment_info = {'add_time': str(comment.add_time), 'comment_content':
             comment.comment_content, 'image': str(user.image), 'nick_name': user.nick_name}
            comment_vo.append(comment_info)

        return JsonResponse({
            'course': serializers.serialize('json', courseQuerySet),
            'comment_vo': json.dumps(comment_vo),
        })


# 机构
sortType(type, cityid, cate) {
  axios({
    url: '/api/orgs/org_list/',
    method: 'GET',
    params: {"keyword": this.keyword, 'sort': type, 'cityid': cityid, 'cate': cate},
  }).then(response => {
    var res = response.data
    this.cityid = res.cityid
    this.keyword = res.keyword
  }).catch(err => {
    console.log(err)
  })
},
getInitAndSearchData() {
  this.keyword = this.$route.query.keyword
  axios({
    url: '/api/orgs/org_list/',
    params: {'keyword': this.keyword},
    method: 'GET'
  }).then(response => {
    var res = response.data
    this.pages = JSON.parse(res.pages)
    this.keyword = res.keyword
    this.showComponent = true
  }).catch(err => {
    console.log(err)
  })
},
},
mounted() {
this.getInitAndSearchData()
},

@cache_page(60 * 24 * 60)
def org_list(request):
    all_orgs = OrgInfo.objects.all().order_by('id')
    all_citys = CityInfo.objects.all().order_by('id')

    # pagination
    page_num = request.GET.get('pagenum', '')
    paginator = Paginator(all_orgs, 3)
    try:
        pages = paginator.page(page_num)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)

    return JsonResponse({
        'all_orgs_count': all_orgs.count(),
        'all_citys': serializers.serialize("json", all_citys),
        'sort_orgs': serializers.serialize("json", sort_orgs),
        'pages': serializers.serialize("json", pages),
        'cate': cate,
        'cityid': cityid,
        'sort': sort,
        'keyword': keyword,
        'has_previous': pages.has_previous(),
        'has_next': pages.has_next(),
        'current_page_number': pages.number,
        'page_range': pages.paginator.num_pages,
    })



# 中间件
class OnlineStatusMiddleware(MiddlewareMixin):
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
        if islogin:
            now = datetime.now()
            lastPath = cache.get(cache_request_path_key)
            this_path = request.path  # 将上一次的 path 缓存到 redis
            if 'get_user' in this_path:
                cache.expire(cache_request_path_key, settings.REDIS_TIMEOUT)
            else:
                cache.set(cache_request_path_key, this_path, settings.REDIS_TIMEOUT)
            this_user = request.user
            userinfo = cache.get(cache_key) # 缓存整个 user 的信息
            if not userinfo:
                cache.set(cache_key, request.user, settings.REDIS_TIMEOUT)
            else:
                cache.expire(cache_key, settings.REDIS_TIMEOUT)
            # 记录 login/logout
            userrecord = UserRecord.objects.filter(user=request.user, type=1).order_by('-start_time')
            if not userrecord:
                ur = UserRecord()
                ...
                ur.save()
            elif 'get_user' in request.path:  # F5
               ...
            # 记录用户所有的点击行为
            if not lastPath or lastPath != this_path:
              ...
        return None
# 定时任务
def job_session_invalid():
    all_cache_key_in_cache = cache.iter_keys("userinfo_*")
    for cache_key in all_cache_key_in_cache:
        expire_time = cache.ttl(cache_key)
        if expire_time < 60 * 4 + 58:
            userinfo = cache.get(cache_key)
            userrecord = UserRecord.objects
              .filter(user=userinfo, end_time=None).order_by('-start_time')
            cache.delete_pattern(cache_key)
            cache_request_path_key = "request_path" + userinfo.username
            cache.delete_pattern(cache_request_path_key)
            for record in userrecord:
                record.end_time = datetime.now()
                record.save()
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
            userrecored = UserRecord.objects
              .filter(month=email_month, user=user)
            if not userrecored:
                send_email_code(user.email, 3)
            else:
                learning_times = userrecored
                  .filter(type=1).count()
                learning_courses_time = userrecored
                  .filter(type=2)
                learning_time = 0
                for record in userrecored:
                    learning_time = learning_time+
                    (record.end_time-record.start_time).seconds
                send_email_code_job(user.email, learning_times,
                   learning_courses_time, learning_time)
    except Exception as e:
        print('发送用户总结任务时出错' + e)



