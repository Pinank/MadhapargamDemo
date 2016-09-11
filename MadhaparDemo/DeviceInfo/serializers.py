from rest_framework import serializers
from .models import DeviceInfo
from gamuser.serializers import UserSerializer

class DeviceInfoSerializer(serializers.ModelSerializer):
	deviceId = serializers.IntegerField(source='device_id')
	deviceInfo = serializers.CharField(source='device_info')
	user = UserSerializer()
	deviceCreatedDate = serializers.DateField(source='device_created_date')
	deviceUpdatedDate = serializers.DateField(source='device_updated_date')

	class Meta:
		model = DeviceInfo
		fields = ['deviceId','deviceInfo','user','deviceCreatedDate','deviceUpdatedDate']