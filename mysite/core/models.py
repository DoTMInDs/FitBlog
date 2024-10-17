from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# from blog.models import Author

# Create your models here.
class ArtistName(models.Model):
    name_of_artist=models.CharField(max_length=100,null=True,unique=True)
    def __str__(self) -> str:
        return self.name_of_artist

class Artist(models.Model):        
    artist_name = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    song_artist_name = models.CharField(max_length=200, null=True,unique=True)
    song_genre = models.CharField(max_length=200, null=True)
    artist_song = models.FileField(upload_to='music/',null=True,blank=True, validators=[FileExtensionValidator(['M4A', 'FLAC', 'MP3', 'WAV', 'MP3'])])
    artist_genre = models.CharField(max_length=200,null=True)
    song_title = models.CharField(null=True,blank=True)
    artist_image=models.ImageField(upload_to='images/',null=True,blank=True)
    artist_profile=models.ImageField(upload_to='images/',null=True,blank=True)
    posted_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return str(self.song_artist_name)
    
class CreateSong(models.Model):    
    artist_name_create = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    song_artist_name_create = models.CharField(max_length=200, null=True,unique=True)
    song_genre_create = models.CharField(max_length=200, null=True)
    artist_song_create = models.FileField(upload_to='music/',null=True,blank=True, validators=[FileExtensionValidator(['M4A', 'FLAC', 'MP3', 'WAV', 'MP3'])])
    artist_genre_create = models.CharField(max_length=200,null=True)
    artist_song_title_create = models.CharField(null=True,blank=True)
    artist_image_create = models.ImageField(upload_to='images/',null=True,blank=True)
    artist_profile_create= models.ImageField(upload_to='images/',null=True,blank=True)
    posted_on_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_on_create']

    def __str__(self):
        return f'{str(self.artist_song_title_create)} by {str(self.song_artist_name_create)}'
    