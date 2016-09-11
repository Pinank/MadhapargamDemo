from rest_framework import serializers
from .models import OTP
from gamuser.serializers import UserSerializer

class OTPSerializer(serializers.ModelSerializer):
	otpId = serializers.IntegerField(source='otp_id')
	user = UserSerializer()
	otp = serializers.CharField()
	otpTimeStamp = serializers.DateTimeField(source='otp_timestamp')

	class Meta:
		model = OTP
		fields = ['otpId', 'user', 'otp', 'otpTimeStamp']