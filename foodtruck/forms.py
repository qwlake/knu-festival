<<<<<<< HEAD
from django import forms
from .models import Foodtruck, Booth

class FoodtruckForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Foodtruck
        exclude = ['user', 'divi']

class BoothForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Booth
=======
from django import forms
from .models import Foodtruck, Booth

class FoodtruckForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Foodtruck
        exclude = ['user', 'divi']

class BoothForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Booth
>>>>>>> a5914912658e8e18fe5ba5a85c0d7df7eeb5d7f0
        exclude = ['user', 'divi']