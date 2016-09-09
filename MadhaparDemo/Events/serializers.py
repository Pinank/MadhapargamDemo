from rest_framework import serializers
from .models import Event, EventAlbum, EventStatusOfUser

class EventSerializer(serializers.ModelSerializer):
	
	class Meta :
		models = Event
		fields = []