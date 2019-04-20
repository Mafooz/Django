from django import forms
from django.contrib.auth.models import User,Group
from .models import Post,Comment
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body','tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['cbody']