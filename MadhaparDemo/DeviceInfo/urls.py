from django.conf.urls import url
from django.contrib import admin
from .views import DeviceInfoList, DeviceDetail

urlpatterns = [
	url(r'^devicelist/$', DeviceInfoList.as_view()),
	url(r'^device-detail/(?P<pk>[0-9]+)/$', DeviceDetail.as_view()),
]