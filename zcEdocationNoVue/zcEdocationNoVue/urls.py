"""zcEducation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from users.views import index

import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # include 分发
    url(r'^captcha/', include('captcha.urls')),
    url(r'^uedit/', include('DjangoUeditor.urls')),
    url(r'^users/', include(('users.urls', 'users'), namespace='users')),
    url(r'^orgs/', include(('orgs.urls', 'orgs'), namespace='orgs')),
    url(r'^operations/', include(('operations.urls', 'operations'), namespace='operations')),
    url(r'^courses/', include(('courses.urls', 'courses'), namespace='courses')),
    url(r'^$', index, name='index'),
]
