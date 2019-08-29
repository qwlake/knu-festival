from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Post
        fields = ('title', 'content', 'password', 'public',)

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('content',)