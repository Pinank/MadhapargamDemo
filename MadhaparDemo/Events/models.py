from __future__ import unicode_literals

from django.db import models
from Location.models import Location
from gamuser.models import UserInfo
from django.utils.crypto import get_random_string

def upload_location(instance, fileName):
	random_string = get_random_string(length=6)
	return "images/%s/%s%s" %(Event._meta.app_label, random_string,".png") 

class Event(models.Model) :
	event_id = models.AutoField(primary_key=True)
	event_name = models.CharField(max_length=20, verbose_name = "Event Title")
	event_from_date = models.DateTimeField(auto_now = False, auto_now_add=False, verbose_name = "Event From")
	event_to_date = models.DateTimeField(auto_now = False, auto_now_add=False, verbose_name = "Event To")
	event_image = models.ImageField('Event Poster', upload_to = upload_location)
	event_organized_by = models.CharField(max_length=50, verbose_name = "Organizers")
	event_location = models.ForeignKey(Location,on_delete=models.CASCADE, verbose_name = "Event Location") 
	event_address = models.CharField(max_length = 150, verbose_name="Address")
	event_chief_guest = models.CharField(max_length = 50, verbose_name="Chief Guest")
	event_description = models.TextField(max_length=2000)
	event_created_date = models.DateField(auto_now = True, auto_now_add=False)
	event_updated_date = models.DateField(auto_now = True, auto_now_add=False)

	def __str__(self):
		return self.event_name

class EventAlbum(models.Model):
	event_album_id = models.AutoField(primary_key=True)
	event_id = models.ForeignKey(Event,on_delete=models.CASCADE, verbose_name="Select Event")
	event_photo = models.ImageField(upload_to = upload_location, verbose_name="Event Photo")
	event_photo_created_date = models.DateField(auto_now = True, auto_now_add=False)
	event_photo_updated_date = models.DateField(auto_now = True, auto_now_add=False)

	def __str__(self):
		return self.event.event_name
		
class EventStatusOfUser(models.Model):
	event_status_id = models.AutoField(primary_key=True)
	event_id = models.ForeignKey(Event,on_delete=models.CASCADE, verbose_name="Select Event")
	user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="Select User")
	event_status_date = models.DateField(auto_now = True, auto_now_add=False)
	EVENT_STATUS_TYPE = (
		('1','Going'),
		('2','Interested'),
		('3','Maybe'),
		)
	event_user_status = models.CharField(max_length=3, choices = EVENT_STATUS_TYPE, default=1)
	event_status_created_date = models.DateField(auto_now = True, auto_now_add=False)
	event_status_updated_date = models.DateField(auto_now = True, auto_now_add=False)

	def __str__(self):
		return self.event.event_name