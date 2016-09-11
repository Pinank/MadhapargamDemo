from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.http import Http404
from Projects.serializers import ProjectAlbumSerializer
from Location.models import Location
from Projects.models import Project, ProjectAlbum
from MadhaparDemo import constant

class ProjectAlbumList(ListCreateAPIView):
	queryset = ProjectAlbum.objects.all()
	serializer_class = ProjectAlbumSerializer
	
	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = ProjectAlbumSerializer(queryset, many=True)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.PROJECT_ALBUM_LIST,
				"response" : serializer.data
			}
		return Response(response)

	def create(self, request, *args, **kwargs):
		projectId = self.request.data.get("projectId")
		project = Project.objects.get(pk=projectId)
		serializer = self.get_serializer(data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save(project=project)
		self.perform_create(serializer)
		response = {
				"status" : status.HTTP_201_CREATED,
				"message" : constant.PROJECT_ALBUM_CREATE,
				"response" : serializer.data
			}
		return Response(response)

class ProjectAlbumDetail(RetrieveUpdateDestroyAPIView) :
	serializer_class = ProjectAlbumSerializer

	def get_object(self, request, *args, **kwargs):
		try:
			return ProjectAlbum.objects.get(pk=kwargs['pk'])
		except Exception, e:
			raise Http404

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		serializer = self.get_serializer(instance)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.PROJECT_ALBUM_DETAIL,
				"response" : serializer.data
			}
		return Response(response)

	def update(self, request, *args, **kwargs):
		projectId = self.request.data.get("projectId")
		instance = self.get_object(self, request, *args, **kwargs)
		serializer = self.get_serializer(instance, data=request.data, partial=True)
		if projectId != None:
			project = Project.objects.get(pk=projectId)
			serializer.is_valid(raise_exception=True)
			serializer.save(project = project)
		else :
			serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.PROJECT_ALBUM_UPDATE,
				"response" : serializer.data
			}
		return Response(response)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		self.perform_destroy(instance)
		response = {
				"status" : status.HTTP_204_NO_CONTENT,
				"message" : constant.PROJECT_ALBUM_DELETE,
			}
		return Response(response)