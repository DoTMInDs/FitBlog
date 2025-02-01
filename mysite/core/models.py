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
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    artist = models.CharField(max_length=200, null=True,unique=True)
    artist_genre = models.CharField(max_length=200,null=True)
    artist_image=models.ImageField(upload_to='images/',null=True,blank=True)
    artist_profile=models.ImageField(upload_to='images/',null=True,blank=True)
    posted_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return str(self.artist)
    
class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='album_covers/', null=True, blank=True)

    class Meta:
        ordering = ['-release_date']

    def __str__(self):
        return self.title
    
class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200, null=True)
    song_file = models.FileField(upload_to='music/', null=True, blank=True, validators=[FileExtensionValidator(['M4A', 'FLAC', 'MP3', 'WAV', 'MP3'])])
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
   
    
class SportsModel(models.Model):
    title=models.CharField(max_length=200, unique=True)
    sub_title=models.CharField(max_length=200, unique=True,null=True)
    artist_song_create = models.FileField(upload_to='video/',null=True,blank=True, validators=[FileExtensionValidator(['MOV', 'WMV', 'MP4', 'FLV', 'WEBM', 'AVI', 'MKV'])])
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    slug=models.SlugField(max_length=200, unique=True)
    article_content=models.TextField(null=True)
    dated_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-dated_on',)

    def __str__(self):
        return self.title