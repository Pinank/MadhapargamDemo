from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
import json


class JSONResponse(HttpResponse):
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['GET'])
def category_list(request, format=None):
	if request.method == 'GET':
		categories = Category.objects.all()
		serializer = CategorySerializer(categories, many=True)
		response = {
			'status': status.HTTP_200_OK,
			'message' : "Category List",
			'response' : serializer.data
		}
		# return HttpResponse(json.dumps(response), content_type='application/json')
		return Response(response)
		# return JSONResponse(response)
	else :
		response = {
			'status' : status.HTTP_400_BAD_REQUEST,
			'message' : "Category not found",
			'response' : serializer.data
		}
		return HttpResponse(json.dumps(response), content_type='application/json')

@api_view(['GET'])
def category_detail(request, pk, format=None):
	try :
		category = Category.objects.get(pk=pk)
	except Category.DoesNotExist :
		response = {
			'status' : status.HTTP_400_BAD_REQUEST,
			'message' : "Category not exist",
		}
		return HttpResponse(json.dumps(response), content_type='application/json')

	if request.method == 'GET' :
		serializer = CategorySerializer(category)
		response = {
			'status': status.HTTP_200_OK,
			'message' : "Category Detail",
			'response' : serializer.data
		}
		return HttpResponse(json.dumps(response), content_type='application/json')

@api_view(['POST'])
def category_add(request):
	if request.method == 'POST':
		serializer = CategorySerializer(data=request.data,partial=True)
		if serializer.is_valid() :
			serializer.save()
			response = {
				'status': status.HTTP_201_CREATED,
				'message' : "Category Added",
				'response' : serializer.data
			}
			return HttpResponse(json.dumps(response), content_type='application/json')
	else :
		response = {
			'status' : status.HTTP_400_BAD_REQUEST,
			'message' : "Category not found",
			'response' : serializer.data
		}
		return HttpResponse(json.dumps(response), content_type='application/json')

@api_view(['PUT'])
def category_update(request, pk):
	try :
		category = Category.objects.get(pk=pk)
	except Category.DoesNotExist :
		response = {
			'status' : status.HTTP_400_BAD_REQUEST,
			'message' : "Category not exist",
		}
		return HttpResponse(json.dumps(response), content_type='application/json')

	if request.method == 'PUT':
		serializer = CategorySerializer(category, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			response = {
				'status': status.HTTP_200_OK,
				'message' : "Category Updated",
				'response' : serializer.data
			}
			return HttpResponse(json.dumps(response), content_type='application/json')
		else :
			response = {
				'status': status.HTTP_400_BAD_REQUEST,
				'message' : "Category not found",
			}
			return HttpResponse(json.dumps(response), content_type='application/json')



@api_view(['DELETE'])
def category_delete(request, pk):
	try :
		category = Category.objects.get(pk=pk)
	except Category.DoesNotExist :
		response = {
			'status' : status.HTTP_400_BAD_REQUEST,
			'message' : "Category not exist",
		}
		return HttpResponse(json.dumps(response), content_type='application/json')

	if request.method == 'DELETE' :
		category.delete()
		response = {
				'status': status.HTTP_204_NO_CONTENT,
				'message' : "Category Deleted",
			}
		return HttpResponse(json.dumps(response), content_type='application/json')