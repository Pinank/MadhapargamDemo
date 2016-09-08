from django.conf.urls import url
from django.contrib import admin
from .views import UserList, UserDetail

urlpatterns = [
	url(r'^users/$', UserList.as_view()),
	url(r'^user-detail/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
]