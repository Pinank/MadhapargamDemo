from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer) :
	class Meta(object):
		"""docstring for Meta"""
		def __init__(self, arg):
			super(Meta, self).__init__()
			self.arg = arg
			