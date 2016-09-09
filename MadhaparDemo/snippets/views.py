from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route

# @api_view(['GET'])
# def api_root(request, format=None):
# 	return Response({
# 		'users': reverse('user-list', request=request, format=format),
# 		'snippets': reverse('snippet-list', request=request, format=format)
# 	})

class SnippetViewSet(viewsets.ModelViewSet):
	"""
	This viewset automatically provides `list`, `create`, `retrieve`,
	`update` and `destroy` actions.

	Additionally we also provide an extra `highlight` action.
	"""
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
	"""
	This viewset automatically provides `list` and `detail` actions.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer


# from .models import Snippet
# from .serializers import SnippetSerializer, UserSerializer
# from rest_framework.generics import ListAPIView, RetrieveAPIView
# from django.contrib.auth.models import User
# from rest_framework import permissions
# from .permissions import IsOwnerOrReadOnly
# from rest_framework import generics
# from rest_framework.decorators import api_view
# from rest_framework.reverse import reverse
# from rest_framework.response import Response
# from rest_framework import renderers

# @api_view(['GET'])
# def api_root(request, format=None):
# 	return Response({
# 		'users': reverse('user-list', request=request, format=format),
# 		'snippets': reverse('snippet-list', request=request, format=format)
# 	})

# class SnippetHighlight(generics.GenericAPIView):
# 	queryset = Snippet.objects.all()
# 	renderer_classes = (renderers.StaticHTMLRenderer,)

# 	def get(self, request, *args, **kwargs):
# 		snippet = self.get_object()
# 		return Response(snippet.highlighted)

# class SnippetList(generics.ListCreateAPIView):
# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer
# 	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# 	def perform_create(self, serializer):
# 		serializer.save(owner=self.request.user)

# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer
# 	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)

# class UserList(ListAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

# class UserDetail(RetrieveAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer

# ============================================

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

class JSONResponse(HttpResponse):
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def snippet_list(request):
	if request.method == 'GET':
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = SnippetSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)

# @csrf_exempt
# def snippet_detail(request, pk):
# 	try:
# 		snippet = Snippet.objects.get(pk=pk)
# 	except Snippet.DoesNotExist:
# 		return HttpResponse(status=404)

# 	if request.method == 'GET':
# 		serializer = SnippetSerializer(snippet)
# 		return JSONResponse(serializer.data)

# 	elif request.method == 'PUT':
# 		data = JSONParser().parse(request)
# 		serializer = SnippetSerializer(snippet, data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JSONResponse(serializer.data)
# 		return JSONResponse(serializer.errors, status=400)

# 	elif request.method == 'DELETE':
# 		snippet.delete()
# 		return HttpResponse(status=204)