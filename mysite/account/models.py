from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.core.validators import FileExtensionValidator # type: ignore


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile', validators=[FileExtensionValidator(['png', 'jpg', 'jfif'])])

    def __str__(self):
        return self.user.username

class UserPostModel(models.Model):
    title=models.CharField(max_length=200, unique=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    post_content=models.TextField()

    def __str__(self):
        return self.title
    