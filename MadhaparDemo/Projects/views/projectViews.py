from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.http import Http404
from Projects.serializers import ProjectSerializer
from Location.models import Location
from Projects.models import Project
from MadhaparDemo import constant

class ProjectList(ListCreateAPIView):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer
	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = ProjectSerializer(queryset, many=True)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.PROJECT_LIST,
				"response" : serializer.data
			}
		return Response(response)

	def create(self, request, *args, **kwargs):
		locationId = self.request.data.get("locationId")
		location = Location.objects.get(pk=locationId)
		serializer = self.get_serializer(data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save(location=location)
		self.perform_create(serializer)
		response = {
				"status" : status.HTTP_201_CREATED,
				"message" : constant.PROJECT_CREATE,
				"response" : serializer.data
			}
		return Response(response)

class ProjectDetail(RetrieveUpdateDestroyAPIView) :
	serializer_class = ProjectSerializer

	def get_object(self, request, *args, **kwargs):
		try:
			return Project.objects.get(pk=kwargs['pk'])
		except Exception, e:
			raise Http404

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		serializer = self.get_serializer(instance)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.PROJECT_DETAIL,
				"response" : serializer.data
			}
		return Response(response)

	def update(self, request, *args, **kwargs):
		locationId = self.request.data.get("locationId")
		instance = self.get_object(self, request, *args, **kwargs)
		serializer = self.get_serializer(instance, data=request.data, partial=True)
		if locationId != None:
			location = Location.objects.get(pk=locationId)
			serializer.is_valid(raise_exception=True)
			serializer.save(location=location)
		else :
			serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.PROJECT_UPDATE,
				"response" : serializer.data
			}
		return Response(response)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		self.perform_destroy(instance)
		response = {
				"status" : status.HTTP_204_NO_CONTENT,
				"message" : constant.PROJECT_DELETE,
			}
		return Response(response)