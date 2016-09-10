from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.http import Http404
from Events.models import Event, EventAlbum, EventStatusOfUser
from Events.serializers import EventSerializer
from Location.models import Location
from MadhaparDemo import constant

class EventList(ListCreateAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer

	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = EventSerializer(queryset, many=True)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.EVENT_LIST,
				"response" : serializer.data
			}
		return Response(response)

	def create(self, request, *args, **kwargs):
		locationId = self.request.data.get("eventLocation")
		location = Location.objects.get(pk=locationId)
		serializer = self.get_serializer(data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save(event_location=location)
		self.perform_create(serializer)
		response = {
				"status" : status.HTTP_201_CREATED,
				"message" : constant.EVENT_CREATE,
				"response" : serializer.data
			}
		return Response(response)

class EventDetail(RetrieveUpdateDestroyAPIView):
	serializer_class = EventSerializer
	def get_object(self, request, *args, **kwargs):
		try:
			return Event.objects.get(pk=kwargs['pk'])
		except Exception, e:
			raise Http404

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		serializer = self.get_serializer(instance)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.EVENT_DETAIL,
				"response" : serializer.data
			}
		return Response(response)

	def update(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		locationId = self.request.data.get("eventLocation")
		serializer = self.get_serializer(instance, data=request.data, partial=True)
		if locationId != None:
			location = Location.objects.get(pk=locationId)
			serializer.is_valid(raise_exception=True)
			serializer.save(user_location_id=location)
		else :
			serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.EVENT_UPDATE,
				"response" : serializer.data
			}
		return Response(response)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		self.perform_destroy(instance)
		response = {
				"status" : status.HTTP_204_NO_CONTENT,
				"message" : constant.EVENT_DELETE,
			}
		return Response(response)