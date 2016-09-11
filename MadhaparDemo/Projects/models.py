from __future__ import unicode_literals
from django.db import models
from Location.models import Location

def upload_location(instance, filename):
	return "%s/%s" %(instance.project_id, filename) 

class Project(models.Model):
	project_id = models.AutoField(primary_key=True)
	project_name = models.CharField(max_length=40, verbose_name = "Project Title")
	project_from_date = models.DateField(auto_now = False, auto_now_add=False)
	project_to_date = models.DateField(auto_now = False, auto_now_add=False)
	project_pic = models.ImageField(upload_to = upload_location, verbose_name="Project Cover")
	width_field = models.IntegerField(default = 0)
	height_field = models.IntegerField(default = 0)
	project_handleby = models.CharField(max_length=40, verbose_name = "Project Manager")
	location = models.ForeignKey(Location,on_delete=models.CASCADE, verbose_name = "Project Location") 
	project_description = models.TextField(max_length=2000)
	project_total_cost = models.PositiveIntegerField()
	project_total_raised = models.PositiveIntegerField()
	project_created_date = models.DateField(auto_now = True, auto_now_add=False)
	project_updated_date = models.DateField(auto_now = True, auto_now_add=False)

	def __str__(self):
		return self.project_name

class ProjectAlbum(models.Model):
	project_album_id = models.AutoField(primary_key=True)
	project = models.ForeignKey(Project,on_delete=models.CASCADE, verbose_name = "Select Project")
	project_photo = models.ImageField(upload_to = upload_location, verbose_name="Project Photo")
	project_photo_created_date = models.DateField(auto_now = True, auto_now_add=False)
	project_photo_updated_date = models.DateField(auto_now = True, auto_now_add=False)

	def __str__(self):
		return self.project.project_name