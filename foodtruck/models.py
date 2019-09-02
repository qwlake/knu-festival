from django.db import models
from django.contrib.auth.models import User

class Foodtruck (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20)
    memo = models.CharField(max_length=30)
    image = models.ImageField()

class Booth (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20)
    memo = models.CharField(max_length=30)
    image = models.ImageField()
