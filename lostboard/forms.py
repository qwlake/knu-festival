from django import forms
from .models import LostPost, Comment

class LostPostForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = LostPost
        fields = ('content', 'image', 'found', 'password',)

    def __init__(self, *args, **kwargs):
        super(LostPostForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('content',)