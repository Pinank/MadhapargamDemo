from __future__ import unicode_literals
from django.db import models
from Location.models import Location
from django.utils.crypto import get_random_string

def upload_location(instance, fileName):
	random_string = get_random_string(length=6)
	return "images/%s/%s%s" %(UserInfo._meta.app_label, random_string,".png") 

class UserInfo(models.Model):
	user_id = models.AutoField(primary_key=True)
	user_firstname = models.CharField(max_length=20, verbose_name = "First Name")
	user_lastname = models.CharField(max_length=20, verbose_name = "Last Name")
	user_email = models.EmailField(max_length=50, verbose_name = "Email Id")
	user_dob = models.DateField(auto_now = False, auto_now_add=False, verbose_name = "Date of Birth")
	user_mobileno = models.CharField(max_length=14, verbose_name = "Contact No")
	user_image = models.ImageField(upload_to = upload_location, verbose_name = "Profile Picture")
	user_password = models.CharField(max_length=20, verbose_name = "Password")
	user_blood_group = models.CharField(max_length=5, verbose_name = "Blood Group")
	user_location_id = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name = "Current Location")
	user_profession = models.CharField(max_length=20, verbose_name = "Profession")
	user_fb_id = models.CharField(max_length=20, verbose_name = "Facebook Contact", blank=True)
	user_random_id = models.CharField(max_length=20, verbose_name = "Registration Id")
	user_created_date = models.DateField(auto_now = True, auto_now_add=False)
	user_updated_date = models.DateField(auto_now = True, auto_now_add=False)

	def get_name(self):
		return "%s %s" % (self.user_firstname, self.user_lastname)

	def __str__(self):
		return "%s %s" % (self.user_firstname, self.user_lastname)