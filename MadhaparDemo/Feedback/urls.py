from django.conf.urls import url
from django.contrib import admin
from .views import FeedbackList, FeedbackDetail

urlpatterns = [
	url(r'^feedbacks/$', FeedbackList.as_view()),
	url(r'^feedback-detail/(?P<pk>[0-9]+)/$', FeedbackDetail.as_view()),
]