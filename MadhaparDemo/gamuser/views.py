from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import UserInfo
from Location.models import Location
from .serializers import UserSerializer
from MadhaparDemo import constant

class UserList(ListCreateAPIView):
	queryset = UserInfo.objects.all()
	serializer_class = UserSerializer

	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = UserSerializer(queryset, many=True)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.MEMBER_LIST,
				"response" : serializer.data
			}
		return Response(response)

	def create(self, request, *args, **kwargs):
		locationId = self.request.data.get("userLocation")
		# name = self.request.data.get("userName")
		location = Location.objects.get(pk=locationId)
		serializer = self.get_serializer(data=request.data, partial=True)
		# firtName = ''
		# lastName = ''
		# if name != None :
		# 	firtName = name.split(' ')[0]
		# 	lastName = name.split(' ')[1]
		serializer.is_valid(raise_exception=True)
		serializer.save(user_location_id=location)
		# serializer.save(user_firstname = firtName , user_lastname = lastName, user_location_id=location)		
		self.perform_create(serializer)
		response = {
				"status" : status.HTTP_201_CREATED,
				"message" : constant.MEMBER_CREATE,
				"response" : serializer.data
			}
		return Response(response)

class UserDetail(RetrieveUpdateDestroyAPIView):
	serializer_class = UserSerializer

	def get_object(self, request, *args, **kwargs):
		try:
			return UserInfo.objects.get(pk=kwargs['pk'])
		except Exception, e:
			raise Http404

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		serializer = self.get_serializer(instance)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.MEMBER_DETAIL,
				"response" : serializer.data
			}
		return Response(response)

	def update(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
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
				"message" : constant.MEMBER_UPDATE,
				"response" : serializer.data
			}
		return Response(response)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		self.perform_destroy(instance)
		response = {
				"status" : status.HTTP_204_NO_CONTENT,
				"message" : constant.MEMBER_DELETE,
			}
		return Response(response)
