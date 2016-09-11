from django.conf.urls import url
from django.contrib import admin
from views.newsfeedViews import NewsFeedList, NewsFeedDetail
from views.newsfeedStatusViews import NewsStausList, NewsStatusDetail

urlpatterns = [
	url(r'^feeds/$', NewsFeedList.as_view()),
	url(r'^feed-detail/(?P<pk>[0-9]+)/$', NewsFeedDetail.as_view()),

	url(r'^feedStatusList/$', NewsStausList.as_view()),
	url(r'^feedStatus-detail/(?P<pk>[0-9]+)/$', NewsStatusDetail.as_view()),
]