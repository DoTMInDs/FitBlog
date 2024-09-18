# from django.contrib.auth.models import User
from django import forms # type: ignore
from .models import PostComment,ArticleComment

class CommentForm(forms.ModelForm):
    post_content = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Add comments here....'}))
    class Meta:
        model = PostComment
        fields = ("post_content",)

class ArticleCommentForm(forms.ModelForm):
    content = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Add comments here....'}))
    class Meta:
        model = ArticleComment
        fields = ("content",)

