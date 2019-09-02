from django import forms
from .models import Foodtruck, Booth

class FoodtruckForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Foodtruck
        exclude = ['user']

class BoothForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Booth
        exclude = ['user']