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

class LocationList(ListCreateAPIView):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer
	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = LocationSerializer(queryset, many=True)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : "Location List.",
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
				"message" : "Location Created.",
				"response" : serializer.data
			}
		return Response(response)

class LocationDetail(RetrieveUpdateDestroyAPIView) :
	queryset = Location.objects.all()
	serializer_class = LocationSerializer

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : "Location Detail.",
				"response" : serializer.data
			}
		return Response(response)

	def update(self, request, *args, **kwargs):
		# partial = kwargs.pop('partial', False)
		instance = self.get_object()
		# serializer = self.get_serializer(instance, data=request.data, partial=partial)
		serializer = self.get_serializer(instance, data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : "Location Updated.",
				"response" : serializer.data
			}
		return Response(response)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		self.perform_destroy(instance)
		response = {
				"status" : status.HTTP_204_NO_CONTENT,
				"message" : "Location Deleted."
			}
		return Response(response)

# class LocationList(ListModelMixin, CreateModelMixin, GenericAPIView):
# 	queryset = Location.objects.all()
# 	serializer_class = LocationSerializer

# 	def get(self, request, *args, **kwargs):
# 		return self.list(request, *args, **kwargs)

# class LocationDetail(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView) :
# 	queryset = Location.objects.all()
# 	serializer_class = LocationSerializer

	# def get(self, request, *args, **kwargs):
	# 	return self.retrieve(request, *args, **kwargs)

# 	def put(self, request, *args, **kwargs):
# 		return self.update(request, *args, **kwargs)

# 	def delete(self, request, *args, **kwargs):
# 		return self.destroy(request, *args, **kwargs)


# class LocationList(APIView):
	
# 	def get(self, request, format=None):
# 		locations = Location.objects.all()
# 		serializer = LocationSerializer(locations, many=True)
# 		response = {
# 			"status" : status.HTTP_200_OK,
# 			"message" : "Location List",
# 			"response" : serializer.data
# 		}
# 		return Response(response)

# 	def post(self, request, format=None):
# 		serializer = LocationSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			response = {
# 				"status" : status.HTTP_201_CREATED,
# 				"message" : "Location Saved",
# 				"response" : serializer.data
# 			}
# 			return Response(response)
# 		response = {
# 				"status" : status.HTTP_400_BAD_REQUEST,
# 				"message" : "Bad data",
# 				"response" : serializer.errors
# 			}
# 		return Response(response)

# class LocationDetail(APIView) :

# 	def get_object(self, pk):
# 		try:
# 			return Location.objects.get(pk=pk)
# 		except Location.DoesNotExist:
# 			raise Http404

# 	def get(self, request, pk, format=None):
# 		location = self.get_object(pk)
# 		serializer = LocationSerializer(location)
		# response = {
		# 	"status" : status.HTTP_200_OK,
		# 	"message" : "Location Detail",
		# 	"response" : serializer.data
		# }
# 		return Response(response)

# 	def put(self, request, pk, format=None):
# 		location = self.get_object(pk)
# 		serializer = LocationSerializer(location, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			response = {
# 				"status" : status.HTTP_201_CREATED,
# 				"message" : "Location updated",
# 				"response" : serializer.data
# 			}
# 			return Response(response)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	def delete(self, request, pk, format=None):
# 		location = self.get_object(pk)
# 		location.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)