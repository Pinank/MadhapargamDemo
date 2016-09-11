from __future__ import unicode_literals
from django.db import models
from gamuser.models import UserInfo

class Feedback(models.Model):
	feedback_id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name = "User Name")
	feedback_subject = models.CharField(max_length=20, verbose_name = "Subject")
	feedback_description = models.TextField(max_length=2000)
	feedback_date = models.DateField(auto_now = True, auto_now_add=False, verbose_name = "Date")

	def __str__(self):
		return feedback_subject