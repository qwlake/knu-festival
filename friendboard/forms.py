from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    password = forms.CharField(max_length=200, widget=forms.PasswordInput())
    class Meta:
        
        model = Post
        fields = ['content', 'password']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['class'] = 'form-control'
        