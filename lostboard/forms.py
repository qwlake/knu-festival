from django import forms
from .models import LostPost

class LostPostForm(forms.ModelForm):
    class Meta:
        model = LostPost
        fields = ('content', 'image', 'finding')

    def __init__(self, *args, **kwargs):
        super(LostPostForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False