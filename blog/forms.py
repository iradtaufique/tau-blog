from django import forms
from blog.models import Comment

"""ModelForm for handling comments"""
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')