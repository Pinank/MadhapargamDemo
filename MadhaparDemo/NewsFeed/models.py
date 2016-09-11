from __future__ import unicode_literals
from django.db import models
from Location.models import Location
from Category.models import Category
from gamuser.models import UserInfo 

def upload_location(instance, fileName):
	return "%s/%s" %(instance.news_id, fileName) 

class NewsFeed(models.Model):
	news_id = models.AutoField(primary_key=True)
	news_title = models.CharField(max_length=40, verbose_name = 'Headlines')
	news_description = models.TextField(max_length=2000)
	news_image1 = models.ImageField(upload_to = upload_location, verbose_name = 'News Image 1')
	news_image2 = models.ImageField(upload_to = upload_location, verbose_name = 'News Image 2')
	news_image3 = models.ImageField(upload_to = upload_location, verbose_name = 'News Image 3')
	news_image4 = models.ImageField(upload_to = upload_location, verbose_name = 'News Image 4')
	news_image5 = models.ImageField(upload_to = upload_location, verbose_name = 'News Image 5')
	news_location_id = models.ForeignKey(Location, on_delete=models.CASCADE,
	 verbose_name = "News Location")
	news_category = models.ForeignKey(Category,  on_delete=models.CASCADE,
	 verbose_name = "Select Category")
	news_created_date = models.DateField(auto_now = True, auto_now_add=False)
	news_updated_date = models.DateField(auto_now = True, auto_now_add=False)

	def __str__(self):
		return self.news_title

class NewsStatus(models.Model):
	STATUS_CHOICES = (
		('1','Comment'),
		('2','Like'),
		)
	news_status_id = models.AutoField(primary_key=True)
	news_id = models.ForeignKey(NewsFeed, on_delete=models.CASCADE, verbose_name = "Select News")
	user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name = "Select User")
	news_comment = models.CharField(max_length=200, blank=True)
	news_status_date = models.DateField(auto_now = True, auto_now_add=False)
	news_status = models.CharField(max_length=2, choices = STATUS_CHOICES)
	news_status_created_date = models.DateField(auto_now = True, auto_now_add=False)
	news_status_updated_date = models.DateField(auto_now = True, auto_now_add=False)

	def __str__(self):
		return self.news_id.news_title