from __future__ import unicode_literals

from django.db import models

class Location(models.Model):
	location_id = models.AutoField(primary_key=True)
	location_name = models.CharField(max_length=30)
	location_created_date = models.DateField(auto_now = True, auto_now_add=False)
	location_updated_date = models.DateField(auto_now = True, auto_now_add=False)
	
	def __str__(self):
		return self.location_name