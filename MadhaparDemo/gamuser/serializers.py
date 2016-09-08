from rest_framework import serializers
from django.core.serializers.json import Serializer
from .models import UserInfo
from Location.serializers import LocationSerializer

class UserSerializer(serializers.ModelSerializer):
	# id = serializers.IntegerField(source='user_id')
	# name = serializers.CharField(source='get_name')
	# email = serializers.EmailField(source='user_email')
	# dob = serializers.DateField(source='user_dob')
	# contactNo = serializers.CharField(source='user_mobileno')
	# image = serializers.CharField(source='user_image')
	# bloodGroup = serializers.CharField(source='user_blood_group')
	# location = serializers.CharField(source='user_location_id')
	# profession = serializers.CharField(source='user_profession')
	# fbId = serializers.CharField(source='user_fb_id')
	# userId = serializers.CharField(source='user_random_id')
	# location = LocationSerializer(source='user_location_id')

	class Meta:
		model = UserInfo
		fields = ['user_id','get_name' ,'user_email','user_dob','user_mobileno','user_image','user_blood_group','user_profession','user_fb_id','user_random_id','user_location_id']
		# fields = ["id", "name", "email", "dob", "contactNo", "image", "bloodGroup", "location", "profession", "fbId", "userId"]