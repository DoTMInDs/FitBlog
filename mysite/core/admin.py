from django.contrib import admin
from .models import Artist,ArtistName,CreateSong,SportsModel

# Register your models here.
# admin.site.register(SongArtist)
admin.site.register(Artist)
admin.site.register(ArtistName)
admin.site.register(CreateSong)
admin.site.register(SportsModel)