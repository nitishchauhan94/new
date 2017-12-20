from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import (
    shift_list, shift_create, shift_delete, shift_detail, shift_update
)

urlpatterns = [
    url(r'^$', shift_list),
    url(r'^create/$', shift_create),
    url(r'^(?P<id>\d+)/$', shift_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', shift_update, name='update'),

    # url(r'^(?P<id>\d+)/$',shift_detail,name='detail'),
    url(r'^update/$', shift_update),
    url(r'^(?P<id>\d+)/delete/$', shift_delete),
    # url(r'^$',"<appname>.views.<function_name>"),
]
