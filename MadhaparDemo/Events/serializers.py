from rest_framework import serializers
from .models import Event, EventAlbum, EventStatusOfUser
from Location.serializers import LocationSerializer
from gamuser.serializers import UserSerializer

class EventSerializer(serializers.ModelSerializer):
	eventId = serializers.IntegerField(source='event_id')
	eventName = serializers.CharField(source='event_name')
	eventFromDate = serializers.DateTimeField(source='event_from_date')
	eventToDate = serializers.DateTimeField(source='event_to_date')
	eventImage = serializers.ImageField(max_length=100, allow_empty_file=True, source="event_image")
	eventOrganizedBy = serializers.CharField(source='event_organized_by')
	eventLocation = LocationSerializer(source='event_location')
	eventAddress = serializers.CharField(source='event_address')
	eventChiefGuest = serializers.CharField(source='event_chief_guest')
	eventDescription = serializers.CharField(source='event_description')
	eventCreatedDate = serializers.DateField(source='event_created_date')
	eventUpdatedDate = serializers.DateField(source='event_updated_date')

	class Meta:
		model = Event
		fields = ['eventId', 'eventName', 'eventFromDate', 'eventToDate' ,'eventImage',
		'eventOrganizedBy', 'eventLocation','eventAddress','eventChiefGuest','eventDescription',
		'eventCreatedDate','eventUpdatedDate']

class EventAlbumSerializer(serializers.ModelSerializer):
	eventAlbumId = serializers.IntegerField(source='event_album_id')
	event = EventSerializer(source='event_id')
	eventPhoto = serializers.ImageField(max_length=100, allow_empty_file=True, source="event_photo")
	eventPhotoCreatedDate = serializers.DateField(source='event_photo_created_date')
	eventPhotoUpdatedDate = serializers.DateField(source='event_photo_updated_date')

	class Meta:
		model = EventAlbum
		fields = ['eventAlbumId', 'event', 'eventPhoto',
		'eventPhotoCreatedDate','eventPhotoUpdatedDate']

class EventUserStatusSerializer(serializers.ModelSerializer):
	eventStatusId = serializers.IntegerField(source='event_status_id')
	event = EventSerializer(source='event_id')
	user = UserSerializer(source='user_id')
	eventStatusDate = serializers.DateField(source='event_status_date')
	eventUserStatus = serializers.CharField(source='event_user_status')
	eventStatusCreatedDate = serializers.DateField(source='event_status_created_date')
	eventStatusUpdatedDate = serializers.DateField(source='event_status_updated_date')

	class Meta:
		model = EventStatusOfUser
		fields = ['eventStatusId', 'event', 'user', 'eventStatusDate', 'eventUserStatus',
		'eventStatusCreatedDate', 'eventStatusUpdatedDate']