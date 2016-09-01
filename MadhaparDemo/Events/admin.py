from django.contrib import admin
from .models import Event,EventAlbum,EventStatusOfUser

admin.site.register(Event)
admin.site.register(EventAlbum)
admin.site.register(EventStatusOfUser)