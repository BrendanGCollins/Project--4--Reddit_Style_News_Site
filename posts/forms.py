from django import forms
from .models import Post, Comment


# Form for creating or updating posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']


# Form for creating or updating comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
