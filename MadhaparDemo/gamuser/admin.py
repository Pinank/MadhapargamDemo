from django.contrib import admin
from .models import UserInfo

class UserAdmin(admin.ModelAdmin):
	list_display = ('user_firstname', 'user_lastname', 'user_email', 
		'user_dob', 'user_mobileno', 'user_random_id' ,
		'user_profession', 'user_image','user_password')

admin.site.register(UserInfo,UserAdmin)