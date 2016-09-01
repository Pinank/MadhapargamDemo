from django.contrib import admin
from .models import NewsFeed, NewsStatus

admin.site.register(NewsFeed)
admin.site.register(NewsStatus)