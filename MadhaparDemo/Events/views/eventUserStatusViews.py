from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from Events.models import Event, EventAlbum, EventStatusOfUser
from Events.serializers import EventSerializer, EventAlbumSerializer, EventUserStatusSerializer
from Location.models import Location
from gamuser.models import UserInfo
from MadhaparDemo import constant

class EventUserStatusList(ListCreateAPIView):
	queryset = EventStatusOfUser.objects.all()
	serializer_class = EventUserStatusSerializer

	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = EventUserStatusSerializer(queryset, many=True)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.EVENT_USER_STATUS_LIST,
				"response" : serializer.data
			}
		return Response(response)

	def create(self, request, *args, **kwargs):
		eventId = self.request.data.get("eventId")
		userId = self.request.data.get("userId")
		event = Event.objects.get(pk=eventId)
		user = UserInfo.objects.get(pk=userId)
		serializer = self.get_serializer(data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save(event_id=event, user_id=user)
		self.perform_create(serializer)
		response = {
				"status" : status.HTTP_201_CREATED,
				"message" : constant.EVENT_USER_STATUS_CREATE,
				"response" : serializer.data
			}
		return Response(response)

class EventUserStatusDetail(RetrieveUpdateDestroyAPIView):
	serializer_class = EventUserStatusSerializer

	def get_object(self, request, *args, **kwargs):
		try:
			return EventStatusOfUser.objects.get(pk=kwargs['pk'])
		except Exception, e:
			raise Http404

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		serializer = self.get_serializer(instance)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.EVENT_USER_STATUS_DETAIL,
				"response" : serializer.data
			}
		return Response(response)

	def update(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		eventId = self.request.data.get("eventId")
		userId = self.request.data.get("userId")
		serializer = self.get_serializer(instance, data=request.data, partial=True)
		if eventId != None and userId != None:
			event = Event.objects.get(pk=eventId)
			user = UserInfo.objects.get(pk=userId)
			serializer.is_valid(raise_exception=True)
			serializer.save(event_id=event, user_id=user)
		else :
			serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.EVENT_USER_STATUS_UPDATE,
				"response" : serializer.data
			}
		return Response(response)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		self.perform_destroy(instance)
		response = {
				"status" : status.HTTP_204_NO_CONTENT,
				"message" : constant.EVENT_USER_STATUS_DELETE,
			}
		return Response(response)