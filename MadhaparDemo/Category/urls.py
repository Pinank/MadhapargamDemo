from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from .views import category_list, category_add, category_detail, category_delete, category_update

urlpatterns = [
	# 'api.views',
	url(r'^list/$', category_list, name='category-list'),
	url(r'^add/',category_add, name='category-add'),
	url(r'^detail/(?P<pk>[0-9]+)/', category_detail, name='category-detail'),
	url(r'^update/(?P<pk>[0-9]+)/', category_update, name='category-update'),
	url(r'^delete/(?P<pk>[0-9]+)/', category_delete, name='category-delete'),
	]

urlpatterns = format_suffix_patterns(urlpatterns)