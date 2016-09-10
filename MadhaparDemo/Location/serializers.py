from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
	locationId = serializers.IntegerField(source='location_id')
	locationName = serializers.CharField(source='location_name')

	class Meta:
		model = Location
		fields = ["locationId", "locationName"]