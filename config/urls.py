# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from mp_vl_app import views


admin.autodiscover()


urlpatterns = [

    ## primary app urls...
    url( r'^info/$', views.info, name='info_url' ),  # home page
    url( r'^db_list/$', views.db_list, name='db_list_url' ),  # behind shib
    url( r'^entry/(?P<id>.*)/$', views.entry, name='entry_url' ),  # behind shib
    url( r'^admin/', admin.site.urls ),  # eg host/project_x/admin/
    # url( r'^admin/login/', RedirectView.as_view(pattern_name='login_url') ),

    ## api urls (all behind auth)...
    url( r'^api/entries/$', views.api_entries, name='api_entries_url' ),
    url( r'^api/entry/(?P<id>.*)/$', views.api_entry, name='api_entry_url' ),

    ## support urls...
    url( r'^login/$', views.login, name='login_url' ),
    url( r'^logout/$', views.logout, name='logout_url' ),
    url( r'^version/$', views.version, name='version_url' ),
    url( r'^error_check/$', views.error_check, name='error_check_url' ),

    ## other...
    url( r'^react_experimentation_01/$', views.exp_01, name='exp_01_url' ),
    url( r'^react_experimentation_02/$', views.exp_02, name='exp_02_url' ),
    url( r'^react_experimentation_03/$', views.exp_03, name='exp_03_url' ),
    url( r'^react_experimentation_04/$', views.exp_04, name='exp_04_url' ),

    url( r'^$', RedirectView.as_view(pattern_name='info_url') ),

    ]
