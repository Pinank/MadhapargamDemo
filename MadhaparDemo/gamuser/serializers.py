from rest_framework import serializers
from django.core.serializers.json import Serializer
from .models import UserInfo
from Location.serializers import LocationSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
	userId = serializers.IntegerField(source='user_id')
	# firstName = serializers.CharField(source='user_firstname')
	# lastName = serializers.CharField(source='user_lastname')
	name = serializers.CharField(source='get_name', read_only=True)
	userEmail = serializers.EmailField(source='user_email')
	userDob = serializers.DateField(source='user_dob')
	userMobileNo = serializers.CharField(source='user_mobileno')
	userImage = serializers.ImageField(max_length=10, allow_empty_file=True, source="user_image")
	userBloodGroup = serializers.CharField(source='user_blood_group')
	userLocation = LocationSerializer(source='user_location_id')
	userProfession = serializers.CharField(source='user_profession')
	userFbId = serializers.CharField(source='user_fb_id')
	userRegId = serializers.CharField(source='user_random_id')

	class Meta:
		model = UserInfo
		fields = ["userId","name", "userEmail", "userDob", "userMobileNo",  "userImage", 
		"userBloodGroup", "userLocation", "userProfession", "userFbId", "userRegId"]