from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Post
        fields = ('content', 'image', 'found', 'password',)

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('content',)