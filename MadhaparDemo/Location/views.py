from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import generics
from django.http import Http404
from .models import Location
from .serializers import LocationSerializer
from MadhaparDemo import constant

class LocationList(ListCreateAPIView):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer
	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = LocationSerializer(queryset, many=True)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.LOCATION_LIST,
				"response" : serializer.data
			}
		return Response(response)

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		# headers = self.get_success_headers(serializer.data)
		response = {
				"status" : status.HTTP_201_CREATED,
				"message" : constant.LOCATION_CREATE,
				"response" : serializer.data
			}
		return Response(response)

class LocationDetail(RetrieveUpdateDestroyAPIView) :
	serializer_class = LocationSerializer

	def get_object(self, request, *args, **kwargs):
		try:
			return Location.objects.get(pk=kwargs['pk'])
		except Exception, e:
			raise Http404

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		serializer = self.get_serializer(instance)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.LOCATION_DETAIL,
				"response" : serializer.data
			}
		return Response(response)

	def update(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		serializer = self.get_serializer(instance, data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.LOCATION_UPDATE,
				"response" : serializer.data
			}
		return Response(response)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		self.perform_destroy(instance)
		response = {
				"status" : status.HTTP_204_NO_CONTENT,
				"message" : constant.LOCATION_DELETE,
			}
		return Response(response)