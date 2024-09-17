from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))
    
class Author(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Profile(models.Model):
    fullname = models.CharField(max_length=100)
    email=models.EmailField(validators=[EmailValidator])
    phone=models.CharField(max_length=20)
    def __str__(self) -> str:
        return f'{self.fullname} {self.email}'
    

class PostModel(models.Model):
    title=models.CharField(max_length=200, unique=True)
    slug=models.SlugField(max_length=200, unique=True)
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    content=models.TextField()
    status=models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return self.title
    
class ArticlePostModel(models.Model):
    title=models.CharField(max_length=200, unique=True)
    sub_title=models.CharField(max_length=200, unique=True,null=True)
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    slug=models.SlugField(max_length=200, unique=True)
    article_content=models.TextField(null=True)
    dated_on=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ('-dated_on',)
    
    def __str__(self):
        return self.title