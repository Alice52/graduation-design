from django.shortcuts import render
from .models import OrgInfo, TeacherInfo, CityInfo
from courses.models import CourseInfo
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from operations.models import UserLove
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers
from users.models import UserProfile


# Create your views here.
def org_list(request):
    all_orgs = OrgInfo.objects.all().order_by('id')
    all_citys = CityInfo.objects.all().order_by('id')

    # 全局搜索功能的过滤
    keyword = request.GET.get('keyword', '')
    if keyword:
        all_orgs = all_orgs.filter(
            Q(name__icontains=keyword) | Q(desc__icontains=keyword) | Q(detail__icontains=keyword))

    # category
    cate = request.GET.get('cate', '')
    if cate:
        all_orgs = all_orgs.filter(category=cate)

    cityid = request.GET.get('cityid', '')
    if cityid:
        all_orgs = all_orgs.filter(cityinfo_id=int(cityid))

    sort = request.GET.get('sort', '')
    if sort:
        all_orgs = all_orgs.order_by('-' + sort)

    sort_orgs = all_orgs.order_by('-love_num')[:5]
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


def org_header(request, org_id):
    orgQuerySet = OrgInfo.objects.filter(id=int(org_id))

    user = None
    u = UserProfile.objects.filter(username=request.user.username)
    if u.count() > 0:
        user = serializers.serialize("json", u),

    lovestatus = False
    if request.user.is_authenticated():
        love = UserLove.objects.filter(love_man=request.user, love_id=int(org_id), love_type=1, love_status=True)
        if love:
            lovestatus = True

    return JsonResponse({
            'user': user,
            'lovestatus': lovestatus,
            'org': serializers.serialize('json', orgQuerySet),
        })

def org_detail(request, org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=int(org_id))[0]

        org.click_num += 1
        org.save()

        # 在返回页面数据的时候，需要返回收藏这个机构的状态，根据状态让模板页面显示收藏还是取消收藏。而不能让页面固定显示收藏。
        lovestatus = False
        if request.user.is_authenticated():
            love = UserLove.objects.filter(love_man=request.user, love_id=int(org_id), love_type=1, love_status=True)
            if love:
                lovestatus = True



        return render(request, 'orgs/org-detail-homepage.html', {
            'org': org,
            'detail_type': 'home',
            'lovestatus': lovestatus
        })


def org_detail_course(request, org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=int(org_id))[0]
        all_courses = org.courseinfo_set.all()

        lovestatus = False
        if request.user.is_authenticated():
            love = UserLove.objects.filter(love_man=request.user, love_id=int(org_id), love_type=1, love_status=True)
            if love:
                lovestatus = True

        # 分页功能
        pagenum = request.GET.get('pagenum', '')
        pa = Paginator(all_courses, 4)
        try:
            pages = pa.page(pagenum)
        except PageNotAnInteger:
            pages = pa.page(1)
        except EmptyPage:
            pages = pa.page(pa.num_pages)
        return render(request, 'orgs/org-detail-course.html', {
            'org': org,
            'pages': pages,
            'detail_type': 'course',
            'lovestatus': lovestatus
        })


def org_detail_desc(request, org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=int(org_id))[0]

        lovestatus = False
        if request.user.is_authenticated():
            love = UserLove.objects.filter(love_man=request.user, love_id=int(org_id), love_type=1, love_status=True)
            if love:
                lovestatus = True

        return render(request, 'orgs/org-detail-desc.html', {
            'org': org,
            'detail_type': 'desc',
            'lovestatus': lovestatus
        })


def org_detail_teacher(request, org_id):
    if org_id:
        org = OrgInfo.objects.filter(id=int(org_id))[0]

        lovestatus = False
        if request.user.is_authenticated():
            love = UserLove.objects.filter(love_man=request.user, love_id=int(org_id), love_type=1, love_status=True)
            if love:
                lovestatus = True

        return render(request, 'orgs/org-detail-teachers.html', {
            'org': org,
            'detail_type': 'teacher',
            'lovestatus': lovestatus
        })


def teacher_list(request):
    all_teachers = TeacherInfo.objects.all().order_by('id')
    sort_teachers = all_teachers.order_by('-love_num')[:4]

    # 全局搜索功能的过滤
    keyword = request.GET.get('keyword', '')
    if keyword:
        all_teachers = all_teachers.filter(name__icontains=keyword)

    sort = request.GET.get('sort', '')
    if sort:
        all_teachers = all_teachers.order_by('-' + sort)

    pagenum = request.GET.get('pagenum', '')
    pa = Paginator(all_teachers, 4)
    try:
        pages = pa.page(pagenum)
    except PageNotAnInteger:
        pages = pa.page(1)
    except EmptyPage:
        pages = pa.page(pa.num_pages)

    return JsonResponse({
        'all_teachers_count': all_teachers.count(),
        'sort_teachers':  serializers.serialize("json", sort_teachers),
        'pages': serializers.serialize("json", pages),
        'sort': sort,
        'keyword': keyword,
        'has_previous': pages.has_previous(),
        'has_next': pages.has_next(),
        'current_page_number': pages.number,
        'page_range': pages.paginator.num_pages,
    })


def teacher_detail(request, teacher_id):
    if teacher_id:
        all_teachers = TeacherInfo.objects.all()
        teacherQuerySet = TeacherInfo.objects.filter(id=int(teacher_id))
        teacher = teacherQuerySet[0]
        sort_teachers = all_teachers.order_by('-love_num')[:3]

        teacher.click_num += 1
        teacher.save()

        loveteacher = False
        loveorg = False
        if request.user.is_authenticated():
            love = UserLove.objects.filter(love_id=int(teacher_id), love_type=3, love_status=True, love_man=request.user)
            if love:
                loveteacher = True
            love1 = UserLove.objects.filter(love_id=teacher.work_company.id, love_type=1, love_status=True, love_man=request.user)
            if love1:
                loveorg = True

        org = OrgInfo.objects.filter(teacherinfo=teacher)[0]
        org_name = org.name
        org_desc = org.desc
        org_id = org.id
        org_img = str(org.image)
        org_address = org.address
        all_courses = CourseInfo.objects.filter(teacherinfo=teacher)

        return JsonResponse({
            'teacher': serializers.serialize('json', teacherQuerySet),
            'sort_teachers': serializers.serialize('json', sort_teachers),
            'loveteacher': loveteacher,
            'loveorg': loveorg,
            'all_courses': serializers.serialize('json', all_courses),
            'org_name': org_name,
            'org_desc': org_desc,
            'org_id': org_id,
            'org_img': org_img,
            'org_address': org_address,
        })
