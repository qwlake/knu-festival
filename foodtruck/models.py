from django.db import models

class Foodtruck (models.Model):
    name = models.CharField(max_length=20)
    memo = models.CharField(max_length=30)

class Booth (models.Model):
    name = models.CharField(max_length=20)
    memo = models.CharField(max_length=30)

