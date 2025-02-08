from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.core.validators import FileExtensionValidator

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
    image=models.ImageField(upload_to='images/',null=True,blank=True, validators=[FileExtensionValidator(['png', 'jpg','jpeg', 'WebP', 'avif', 'jfif'])])
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    content=models.TextField()
    status=models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ('-created_on',)

    def post_comment_count(self):
        return self.postcomment_set.all().count()
    
    def post_comments(self):
        return self.postcomment_set.all()

    def __str__(self):
        return self.title
    
class ArticlePostModel(models.Model):
    title=models.CharField(max_length=200, unique=True)
    sub_title=models.CharField(max_length=200, unique=True,null=True)
    image=models.ImageField(upload_to='images/',null=True,blank=True, validators=[FileExtensionValidator(['png', 'jpg','jpeg', 'WebP', 'avif', 'jfif'])])
    author=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    slug=models.SlugField(max_length=200, unique=True)
    article_content=models.TextField(null=True)
    dated_on=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ('-dated_on',)
    
    def article_comment_count(self):
        return self.articlecomment_set.all().count()
    
    def article_comments(self):
        return self.articlecomment_set.all()
    
    def __str__(self):
        return self.title

class ArticleComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(ArticlePostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self) :
        return self.content
         
class PostComment(models.Model):
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_com = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    post_content = models.CharField(max_length=200)

    def __str__(self) :
        return self.post_content
         

         