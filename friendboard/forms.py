from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    password = forms.CharField(max_length=200, widget=forms.PasswordInput())
    class Meta:
        
        model = Post
        fields = ['content', 'password']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs['class'] = 'form-control'

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('content',)