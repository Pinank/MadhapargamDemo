from rest_framework import serializers
from .models import Feedback
from gamuser.serializers import UserSerializer

class FeedbackSerializer(serializers.ModelSerializer):
	feedbackId = serializers.IntegerField(source='feedback_id')
	user = UserSerializer(source='user_id')
	feedbackSubject = serializers.CharField(source='feedback_subject')
	feedbackDescription = serializers.CharField(source='feedback_description')
	feedbackDate = serializers.DateField(source='feedback_date')

	class Meta:
		model = Feedback
		fields = ['feedbackId', 'user', 'feedbackSubject', 'feedbackDescription' ,'feedbackDate']