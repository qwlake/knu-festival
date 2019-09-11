import os
from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=False)
    public = models.BooleanField(default=True)
    password = models.CharField(null=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("{}").format(self.title)

class Comment(models.Model):
    qnapost = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
