from django.contrib import admin
from .models import Profile,Author,PostModel,ArticlePostModel
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import User


class ProfileAdmin(admin.ModelAdmin):
    list_display=['fullname','phone','email']
    readonly_fields=['fullname','phone','email']

# Register your models here.
admin.site.register(Profile,ProfileAdmin)
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Author)
admin.site.register(PostModel)
admin.site.register(ArticlePostModel)
