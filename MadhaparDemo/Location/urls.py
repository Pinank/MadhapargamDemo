from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from .views import LocationList, LocationDetail

urlpatterns = [
	url(r'^locations/$', LocationList.as_view()),
	url(r'^location-detail/(?P<pk>[0-9]+)/$', LocationDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)