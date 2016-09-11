from rest_framework import serializers
from .models import Project, ProjectAlbum
from Location.serializers import LocationSerializer

class ProjectSerializer(serializers.ModelSerializer):
	projectId = serializers.IntegerField(source='project_id')
	projectName= serializers.CharField(source='project_name')
	projectFromDate = serializers.DateTimeField(source='project_from_date')
	projectToDate = serializers.DateTimeField(source='project_to_date')
	projectPic = serializers.ImageField(source='project_pic',max_length=10, allow_empty_file=False)
	projectHandleby = serializers.CharField(source='project_handleby')
	location = LocationSerializer()
	projectDescription = serializers.CharField(source='project_description')
	projectTotalCost = serializers.IntegerField(source='project_total_cost')
	projectTotalRaised = serializers.IntegerField(source='project_total_raised')
	projectCreatedDate = serializers.DateField(source='project_created_date')
	projectUpdatedDate = serializers.DateField(source='project_updated_date')
	
	class Meta:
		model = Project
		fields = ['projectId', 'projectName', 'projectFromDate', 'projectToDate', 'projectPic',
		'projectHandleby','location','projectDescription','projectTotalCost','projectTotalRaised',
		'projectCreatedDate','projectUpdatedDate']


class ProjectAlbumSerializer(serializers.ModelSerializer):
	projectAlbumId = serializers.IntegerField(source='project_album_id')
	project = ProjectSerializer()
	projectPhoto = serializers.ImageField(source='project_photo',max_length=10, allow_empty_file=False)
	projectPhotoCreatedDate = serializers.DateField(source='project_photo_created_date')
	projectPhotoUpdatedDate = serializers.DateField(source='project_photo_updated_date')

	class Meta:
		model = ProjectAlbum
		fields = ['projectAlbumId', 'project', 'projectPhoto', 'projectPhotoCreatedDate',
		'projectPhotoUpdatedDate']