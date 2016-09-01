from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
	category_id = models.AutoField(primary_key=True)
	category_name = models.CharField("Category Name", max_length = 30)
	category_created_date = models.DateField(auto_now = True, auto_now_add=False)
	category_updated_date = models.DateField(auto_now = True, auto_now_add=False)

	def __str__(self):
		return self.category_name