from django.db import models
from django.contrib.auth.models import User

class Foodtruck (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True)
    divi = models.IntegerField()    #divi: {1:육주}, {2:함광}, {3:미광}
    ftimage= models.ImageField(null=True, blank=True)

class Booth (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True)
    divi = models.IntegerField()
    btimage= models.ImageField(null=True, blank=True)
