from django.contrib import admin
from .models import Artist,Song,ArtistName,Album,SportsModel

# Register your models here.
# admin.site.register(SongArtist)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(ArtistName)
admin.site.register(Album)
admin.site.register(SportsModel)