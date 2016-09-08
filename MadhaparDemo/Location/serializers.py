from rest_framework import serializers
from django.core.serializers.json import Serializer
from .models import Location
from gamuser.models import UserInfo

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = ["location_id", "location_name"]