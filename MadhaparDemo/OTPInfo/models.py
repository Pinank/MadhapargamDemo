from __future__ import unicode_literals
from django.db import models
from gamuser.models import UserInfo

class OTP(models.Model):
	otp_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(UserInfo, on_delete=models.CASCADE,verbose_name = "User Name")
	otp = models.PositiveIntegerField()
	otp_timestamp = models.DateTimeField(auto_now = True, auto_now_add=False)

	def __str__(self):
		return otp