from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Feedback
from gamuser.models import UserInfo
from .serializers import FeedbackSerializer
from MadhaparDemo import constant

class FeedbackList(ListCreateAPIView):
	queryset = Feedback.objects.all()
	serializer_class = FeedbackSerializer

	def list(self, request, *args, **kwargs):
		queryset = self.get_queryset()
		serializer = FeedbackSerializer(queryset, many=True)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.FEEDBACK_LIST,
				"response" : serializer.data
			}
		return Response(response)

	def create(self, request, *args, **kwargs):
		userId = self.request.data.get("userId")
		user = UserInfo.objects.get(pk=userId)
		serializer = self.get_serializer(data=request.data, partial=True)
		serializer.is_valid(raise_exception=True)
		serializer.save(user_id=user)
		self.perform_create(serializer)
		response = {
				"status" : status.HTTP_201_CREATED,
				"message" : constant.FEEDBACK_CREATE,
				"response" : serializer.data
			}
		return Response(response)

class FeedbackDetail(RetrieveUpdateDestroyAPIView):
	serializer_class = FeedbackSerializer

	def get_object(self, request, *args, **kwargs):
		try:
			return Feedback.objects.get(pk=kwargs['pk'])
		except Exception, e:
			raise Http404

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		serializer = self.get_serializer(instance)
		response = {
				"status" : status.HTTP_200_OK,
				"message" : constant.FEEDBACK_DETAIL,
				"response" : serializer.data
			}
		return Response(response)

	def update(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		userId = self.request.data.get("userId")
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
				"message" : constant.FEEDBACK_UPDATE,
				"response" : serializer.data
			}
		return Response(response)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object(self, request, *args, **kwargs)
		self.perform_destroy(instance)
		response = {
				"status" : status.HTTP_204_NO_CONTENT,
				"message" : constant.FEEDBACK_DELETE,
			}
		return Response(response)
