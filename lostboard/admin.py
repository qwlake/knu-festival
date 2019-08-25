from django.contrib import admin
from .models import LostPost, Comment

admin.site.register(LostPost)
admin.site.register(Comment)