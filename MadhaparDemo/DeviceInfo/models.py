from __future__ import unicode_literals

from django.db import models
from gamuser.models import UserInfo

class DeviceInfo(models.Model):
	device_id = models.AutoField(primary_key=True)
	device_info = models.CharField(max_length=32, verbose_name="Device Token")
	user = models.ForeignKey(UserInfo, on_delete=models.CASCADE,verbose_name = "User Name")
	device_created_date = models.DateField(auto_now = True, auto_now_add=False)
	device_updated_date = models.DateField(auto_now = True, auto_now_add=False)

	def __str__(self):
		return device_info