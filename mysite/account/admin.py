from django.contrib import admin
from .models import ProfileModel,UserPostModel

# Register your models here.
admin.site.register(ProfileModel)
admin.site.register(UserPostModel)