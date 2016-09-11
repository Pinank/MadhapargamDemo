from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.http import Http404
from Location.models import Location
from Category.models import Category
from NewsFeed.models import NewsFeed
from NewsFeed.serializers import NewsFeedSerializer
from MadhaparDemo import constant

class NewsFeedList(ListCreateAPIView):
	queryset = NewsFeed.objects.all()
	serializer_class = NewsFeedSerializer

	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = NewsFeedSerializer(queryset, many=True)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.NEWSFEED_LIST,
				"response" : serializer.data
			}
		return Response(response)

	def create(self, request, *args, **kwargs):
		locationId = self.request.data.get("newsLocationId")
		newsCategoryId = self.request.data.get("newsCategoryId")
		location = Location.objects.get(pk=locationId)
		category = Category.objects.get(pk=newsCategoryId)
		serializer = self.get_serializer(data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save(news_location_id=location, news_category=category)
		self.perform_create(serializer)
		response = {
				"status" : status.HTTP_201_CREATED,
				"message" : constant.NEWSFEED_CREATE,
				"response" : serializer.data
			}
		return Response(response)

class NewsFeedDetail(RetrieveUpdateDestroyAPIView):
	serializer_class = NewsFeedSerializer
	def get_object(self, request, *args, **kwargs):
		try:
			return NewsFeed.objects.get(pk=kwargs['pk'])
		except Exception, e:
			raise Http404

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		serializer = self.get_serializer(instance)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.NEWSFEED_DETAIL,
				"response" : serializer.data
			}
		return Response(response)

	def update(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		locationId = self.request.data.get("newsLocationId")
		serializer = self.get_serializer(instance, data=request.data, partial=True)
		if locationId != None:
			location = Location.objects.get(pk=locationId)
			serializer.is_valid(raise_exception=True)
			serializer.save(news_location_id=location)
		else :
			serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.NEWSFEED_UPDATE,
				"response" : serializer.data
			}
		return Response(response)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		self.perform_destroy(instance)
		response = {
				"status" : status.HTTP_204_NO_CONTENT,
				"message" : constant.NEWSFEED_DELETE,
			}
		return Response(response)