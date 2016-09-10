from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from Events.models import Event, EventAlbum, EventStatusOfUser
from Events.serializers import EventSerializer, EventAlbumSerializer, EventUserStatusSerializer
from Location.models import Location
from MadhaparDemo import constant

class EventAlbumList(ListCreateAPIView):
	queryset = EventAlbum.objects.all()
	serializer_class = EventAlbumSerializer

	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = EventAlbumSerializer(queryset, many=True)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.EVENT_ALBUM_LIST,
				"response" : serializer.data
			}
		return Response(response)

	def create(self, request, *args, **kwargs):
		eventId = self.request.data.get("event")
		event = Event.objects.get(pk=eventId)
		serializer = self.get_serializer(data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save(event_id=event)
		self.perform_create(serializer)
		response = {
				"status" : status.HTTP_201_CREATED,
				"message" : constant.EVENT_ALBUM_CREATE,
				"response" : serializer.data
			}
		return Response(response)

class EventAlbumDetail(RetrieveUpdateDestroyAPIView):
	serializer_class = EventAlbumSerializer

	def get_object(self, request, *args, **kwargs):
		try:
			return EventAlbum.objects.get(pk=kwargs['pk'])
		except Exception, e:
			raise Http404

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		serializer = self.get_serializer(instance)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.EVENT_ALBUM_DETAIL,
				"response" : serializer.data
			}
		return Response(response)

	def update(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		eventId = self.request.data.get("event")
		serializer = self.get_serializer(instance, data=request.data, partial=True)
		if eventId != None:
			event = Event.objects.get(pk=eventId)
			serializer.is_valid(raise_exception=True)
			serializer.save(event_id=event)
		else :
			serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.EVENT_ALBUM_UPDATE,
				"response" : serializer.data
			}
		return Response(response)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		self.perform_destroy(instance)
		response = {
				"status" : status.HTTP_204_NO_CONTENT,
				"message" : constant.EVENT_ALBUM_DELETE,
			}
		return Response(response)