from django.conf.urls import url
from django.contrib import admin
from views.projectViews import ProjectList,ProjectDetail
from views.projectAlbumViews import ProjectAlbumList, ProjectAlbumDetail

urlpatterns = [
	url(r'^projectlist/$', ProjectList.as_view()),
	url(r'^project-detail/(?P<pk>[0-9]+)/$', ProjectDetail.as_view()),

	url(r'^projectAlbumList/$', ProjectAlbumList.as_view()),
	url(r'^projectAlbum-detail/(?P<pk>[0-9]+)/$', ProjectAlbumDetail.as_view()),
]