from rest_framework import serializers
from django.core.serializers.json import Serializer
from .models import UserInfo
from Location.serializers import LocationSerializer

class UserSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(source='user_id')
	fistname = serializers.CharField(source='user_firstname')
	lastname = serializers.CharField(source='user_lastname')
	email = serializers.EmailField(source='user_email')
	dob = serializers.DateField(source='user_dob')
	contactNo = serializers.CharField(source='user_mobileno')
	image = serializers.CharField(source='user_image')
	bloodGroup = serializers.CharField(source='user_blood_group')
	location = LocationSerializer(source='user_location_id')
	profession = serializers.CharField(source='user_profession')
	fbId = serializers.CharField(source='user_fb_id')
	userId = serializers.CharField(source='user_random_id')
	

	class Meta:
		model = UserInfo
		# fields = ['user_id','user_firstname', 'user_lastname' ,'user_email','user_dob','user_mobileno','user_image','user_blood_group','user_profession','user_fb_id','user_random_id','location']
		fields = ["id", "fistname", "lastname", "email", "dob", "contactNo", "image", "bloodGroup", "location", "profession", "fbId", "userId"]