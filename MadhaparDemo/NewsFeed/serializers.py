from rest_framework import serializers
from .models import OTP

class OTPSerializer(serializers.ModelSerializer):
	otpId = serializers.IntegerField(source='otp_id')
	userId = serializers.CharField(source='user.user_id')
	otp = serializers.CharField(source='otp')
	otpTimeStamp = serializers.CharField(source='otp_timestamp')