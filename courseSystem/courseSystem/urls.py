"""
URL configuration for courseSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from index import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('index/', views.index),
    path("course/list/", views.course_list),
    path('course/add/', views.course_add),
    path('course/delete/', views.course_del),
    path('', views.login),
    path('register/', views.register),
    path('course/manage/', views.course_manage),
    path('course/update/', views.course_update),
    path('course/cleck/', views.course_cleck),
    path('dep_list', views.dep_list),
    path('course/register/', views.course_register),
    path('course/detail/',views.course_detail),
]
