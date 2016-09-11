from rest_framework import serializers
from .models import NewsFeed, NewsStatus
from Location.serializers import LocationSerializer
from Category.serializers import CategorySerializer
from gamuser.serializers import UserSerializer

class NewsFeedSerializer(serializers.ModelSerializer):
	newsId = serializers.IntegerField(source='news_id')
	newsTitle = serializers.CharField(source='news_title')
	newsDescription = serializers.CharField(source='news_description')
	newsImage1 = serializers.ImageField(max_length=100, allow_empty_file=True, source="news_image1")
	newsImage2 = serializers.ImageField(max_length=100, allow_empty_file=True, source="news_image2")
	newsImage3 = serializers.ImageField(max_length=100, allow_empty_file=True, source="news_image3")
	newsImage4 = serializers.ImageField(max_length=100, allow_empty_file=True, source="news_image4")
	newsImage5 = serializers.ImageField(max_length=100, allow_empty_file=True, source="news_image5")
	newsLocation = LocationSerializer(source='news_location_id')
	newsCategory = CategorySerializer(source='news_category')
	newsCreatedDate = serializers.DateField(source='news_created_date')
	newsUpdatedDate = serializers.DateField(source='news_updated_date')

	class Meta:
		model = NewsFeed
		fields = ['newsId', 'newsTitle', 'newsDescription', 'newsImage1', 'newsImage2', 'newsImage3', 
		'newsImage4', 'newsImage5', 'newsLocation', 'newsCategory', 'newsCreatedDate', 'newsUpdatedDate']


class NewsStatusSerializer(serializers.ModelSerializer):
	newsStatusId = serializers.IntegerField(source='news_status_id')
	newsComment = serializers.CharField(source='news_comment')
	newsStatusDate = serializers.DateField(source='news_status_date')
	newsStatus = serializers.CharField(source='news_status')
	newsStatusCreatedDate = serializers.DateField(source='news_status_created_date', read_only=True)
	newsStatusUpdatedDate = serializers.DateField(source='news_status_updated_date', read_only=True)
	news = NewsFeedSerializer(source='news_id')
	user = UserSerializer(source='user_id')

	class Meta:
		model = NewsStatus
		fields = ['newsStatusId', 'newsComment', 'newsStatusDate', 'newsStatus', 'newsStatusCreatedDate',
		 'newsStatusUpdatedDate', 'news', 'user']



