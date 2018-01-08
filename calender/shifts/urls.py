from django.conf.urls import url
from django.contrib import admin
from .views import (shift_list,
                    shift_create,
                    shift_detail,
                    shift_update,
                    shift_delete)

urlpatterns = [
    url(r'^$',shift_list),
    url(r'^create/$',shift_create),
    url(r'^(?P<id>\d+)/$',shift_detail,name='detail'),
    url(r'^(?P<id>\d+)/edit/$',shift_update,name='update'),
    url(r'^(?P<id>\d+)/delete/$',shift_delete),
    ]
