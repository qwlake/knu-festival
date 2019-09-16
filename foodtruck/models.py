from django.db import models
from django.contrib.auth.models import User

class Foodtruck (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True)
    divi = models.IntegerField()    #divi: {1:육주}, {2:함광}, {3:미광}
    ftimage = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Booth (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20)
    image = models.ImageField(null=True, blank=True)
    divi = models.IntegerField()
    btimage = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    btimage= models.ImageField(null=True, blank=True)

class menu (models.Model):
    food = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    foodtruck = models.ForeignKey('FoodTruck', on_delete=models.CASCADE, null=False, related_name='menus')

    def __str__(self):
        return self.foodtruck.name

class booth_menu (models.Model):
    food = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    booth = models.ForeignKey('Booth', on_delete=models.CASCADE, null=False, related_name='menus')

    def __str__(self):
        return self.booth.name