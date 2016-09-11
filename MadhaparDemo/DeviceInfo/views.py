from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.http import Http404
from .serializers import DeviceInfoSerializer
from rest_framework.response import Response
from rest_framework import status
from .serializers import DeviceInfoSerializer
from gamuser.models import UserInfo
from .models import DeviceInfo
from MadhaparDemo import constant

class DeviceInfoList(ListCreateAPIView):
	queryset = DeviceInfo.objects.all()
	serializer_class = DeviceInfoSerializer

	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = DeviceInfoSerializer(queryset, many=True)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.DEVICE_LIST,
				"response" : serializer.data
			}
		return Response(response)

	def create(self, request, *args, **kwargs):
		userId = self.request.data.get("userId")
		user = UserInfo.objects.get(pk=userId)
		serializer = self.get_serializer(data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save(user=user)
		self.perform_create(serializer)
		response = {
				"status" : status.HTTP_201_CREATED,
				"message" : constant.DEVICE_CREATE,
				"response" : serializer.data
			}
		return Response(response)

class DeviceDetail(RetrieveUpdateDestroyAPIView):
	serializer_class = DeviceInfoSerializer

	def get_object(self, request, *args, **kwargs):
		try:
			return DeviceInfo.objects.get(pk=kwargs['pk'])
		except Exception, e:
			raise Http404

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		serializer = self.get_serializer(instance)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.DEVICE_DETAIL,
				"response" : serializer.data
			}
		return Response(response)

	def update(self, request, *args, **kwargs):
		userId = self.request.data.get("userId")
		instance = self.get_object(self, request, *args, **kwargs)
		serializer = self.get_serializer(instance, data=request.data, partial=True)
		if userId != None:
			user = UserInfo.objects.get(pk=userId)
			serializer.is_valid(raise_exception=True)
			serializer.save(user=user)
		else :
			serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.DEVICE_UPDATE,
				"response" : serializer.data
			}
		return Response(response)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		self.perform_destroy(instance)
		response = {
				"status" : status.HTTP_204_NO_CONTENT,
				"message" : constant.DEVICE_DELETE,
			}
		return Response(response)