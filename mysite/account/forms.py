# from django.forms import ModelForm
from typing import Any
from django import forms # type: ignore
from .models import ProfileModel
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore

from blog.models import ArticlePostModel


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    
    def __init__(self, *args: Any, **kwargs: Any):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        for fieldname in ["username", "email", "password1", "password2"]:
            self.fields[fieldname].help_text = None 


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ "username", "email"]
    def __init__(self, *args: Any, **kwargs: Any):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for fieldname in [ "username", "email"]:
            self.fields[fieldname].help_text = None

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = [ "full_name", "image", "about", "talks_about"]

class UserPostForm(forms.ModelForm):
    article_content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    class Meta:
        model = ArticlePostModel
        fields = ("title", "sub_title", "article_content", "image", "slug")

class PostEditForm(forms.ModelForm):
    class Meta:
        model = ArticlePostModel
        fields = ("title", "article_content", "image", "slug")
