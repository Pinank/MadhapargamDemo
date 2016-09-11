from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.http import Http404
from NewsFeed.models import NewsFeed, NewsStatus
from gamuser.models import UserInfo
from NewsFeed.serializers import NewsStatusSerializer
from MadhaparDemo import constant

class NewsStausList(ListCreateAPIView):
	queryset = NewsStatus.objects.all()
	serializer_class = NewsStatusSerializer

	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = NewsStatusSerializer(queryset, many=True)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.NEWSFEED_STATUS_LIST,
				"response" : serializer.data
			}
		return Response(response)

	def create(self, request, *args, **kwargs):
		newsId = self.request.data.get("newsId")
		userId = self.request.data.get("userId")
		serializer = self.get_serializer(data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save (
			news_id=NewsFeed.objects.get(pk=newsId),
			user_id=UserInfo.objects.get(pk=userId)
			)
		self.perform_create(serializer)
		response = {
				"status" : status.HTTP_201_CREATED,
				"message" : constant.NEWSFEED_STATUS_CREATE,
				"response" : serializer.data
			}
		return Response(response)

class NewsStatusDetail(RetrieveUpdateDestroyAPIView):
	serializer_class = NewsStatusSerializer
	def get_object(self, request, *args, **kwargs):
		try:
			return NewsStatus.objects.get(pk=kwargs['pk'])
		except Exception, e:
			raise Http404

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		serializer = self.get_serializer(instance)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.NEWSFEED_STATUS_DETAIL,
				"response" : serializer.data
			}
		return Response(response)

	def update(self, request, *args, **kwargs):
		newsId = self.request.data.get("newsId")
		userId = self.request.data.get("userId")
		instance = self.get_object(self, request, *args, **kwargs)
		serializer = self.get_serializer(instance, data=request.data, partial=True)
		if newsId != None and userId != None:
			news = NewsFeed.objects.get(pk=newsId)
			user = UserInfo.objects.get(pk=userId)
			serializer.is_valid(raise_exception=True)
			serializer.save(user_id=user, news_id=news)
		else :
			serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.NEWSFEED_STATUS_UPDATE,
				"response" : serializer.data
			}
		return Response(response)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		self.perform_destroy(instance)
		response = {
				"status" : status.HTTP_204_NO_CONTENT,
				"message" : constant.NEWSFEED_STATUS_DELETE,
			}
		return Response(response)