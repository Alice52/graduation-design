from django.shortcuts import render
from .models import OrgInfo, TeacherInfo, CityInfo
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def org_list(request):
    all_orgs = OrgInfo.objects.all()
    all_citys = CityInfo.objects.all()
    sort_orgs = all_orgs.order_by('-love_num')[:3]

    page_num = request.GET.get('pagenum', '')
    paginator = Paginator(all_orgs, 3)
    try:
        pages = paginator.page(page_num)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(paginator.num_pages)

    return render(request, 'org-list.html', {
        'all_orgs': all_orgs,
        'all_citys': all_citys,
        'sort_orgs': sort_orgs,
        'pages': pages,
    })
