from rest_framework import serializers
from django.core.serializers.json import Serializer

from .models import Category

class CategorySerializer(serializers.ModelSerializer) :
	id = serializers.IntegerField(source='category_id')
	name = serializers.CharField(source='category_name')

	class Meta:
		model = Category
		fields = ['id', 'name']