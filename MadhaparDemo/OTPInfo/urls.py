from django.conf.urls import url
from django.contrib import admin
from .views import OTPList, OTPDetail
urlpatterns = [
	url(r'^otplist/$', OTPList.as_view()),
	url(r'^otp-detail/(?P<pk>[0-9]+)/$', OTPDetail.as_view()),
]