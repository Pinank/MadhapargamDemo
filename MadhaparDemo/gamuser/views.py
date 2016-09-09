from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import generics
from django.http import Http404
from .models import UserInfo
from Location.models import Location
from .serializers import UserSerializer

class UserList(ListCreateAPIView):
	queryset = UserInfo.objects.all()
	serializer_class = UserSerializer

	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = UserSerializer(queryset, many=True)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : "User List.",
				"response" : serializer.data
			}
		return Response(response)

	def create(self, request, *args, **kwargs):
		locationId = self.request.data.get("userLocation")
		name = self.request.data.get("name")
		location = Location.objects.get(pk=locationId)
		serializer = self.get_serializer(data=request.data, partial=True)
		firtName = ''
		lastName = ''
		if name != None :
			firtName = name.split(' ')[0]
			lastName = name.split(' ')[1]
		serializer.is_valid(raise_exception=True)
		print("------------------>",firtName)
		print("------------------>",lastName)
		serializer.save(user_firstname = firtName , user_lastname = lastName, user_location_id=location)		
		self.perform_create(serializer)
		response = {
				"status" : status.HTTP_201_CREATED,
				"message" : "User Created.",
				"response" : serializer.data
			}
		return Response(response)

class UserDetail(RetrieveUpdateDestroyAPIView):
	queryset = UserInfo.objects.all()
	serializer_class = UserSerializer

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : "User Detail.",
				"response" : serializer.data
			}
		return Response(response)

	def update(self, request, *args, **kwargs):
		instance = self.get_object()
		locationId = self.request.data.get("userLocation")
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
				"message" : "User Detail Updated.",
				"response" : serializer.data
			}
		return Response(response)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		self.perform_destroy(instance)
		response = {
				"status" : status.HTTP_204_NO_CONTENT,
				"message" : "User Deleted."
			}
		return Response(response)
