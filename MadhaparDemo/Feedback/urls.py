from django.conf.urls import url
from django.contrib import admin
from views.eventViews import EventList, EventDetail
from views.eventAlbumViews import EventAlbumList, EventAlbumDetail
from views.eventUserStatusViews import EventUserStatusList, EventUserStatusDetail

urlpatterns = [
	url(r'^events/$', EventList.as_view()),
	url(r'^event-detail/(?P<pk>[0-9]+)/$', EventDetail.as_view()),

	url(r'^eventAlbums/$', EventAlbumList.as_view()),
	url(r'^eventAlbumDetail/(?P<pk>[0-9]+)/$', EventAlbumDetail.as_view()),

	url(r'^eventUserStatus/$', EventUserStatusList.as_view()),
	url(r'^eventUserStatusDetail/(?P<pk>[0-9]+)/$', EventUserStatusDetail.as_view()),
]