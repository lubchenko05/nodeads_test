# api/urls.py
from django.urls import re_path

from .views import ElementDetailView, ElementView, ElementByGroupView, GroupDetailView, GroupView

urlpatterns = [
    re_path(r'^groups/$', GroupView.as_view(), name='group-list'),
    re_path(r'^groups/(?P<pk>[0-9]+)/$', GroupDetailView.as_view(), name='group-detail'),
    re_path(r'^groups/(?P<group_pk>[0-9]+)/elements/$', ElementByGroupView.as_view(), name='group-elements'),
    re_path(r'^elements/$', ElementView.as_view(), name='element-list'),
    re_path(r'^elements/(?P<pk>[0-9]+)/$', ElementDetailView.as_view(), name='element-detail'),
]