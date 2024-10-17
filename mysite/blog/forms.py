# from django.contrib.auth.models import User
from django import forms # type: ignore
from .models import PostComment,ArticleComment

from core.models import Artist,ArtistName,CreateSong

class CommentForm(forms.ModelForm):
    post_content = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Add comments here....'}))
    class Meta:
        model = PostComment
        fields = ("post_content",)

class ArticleCommentForm(forms.ModelForm):
    content = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Add comments here....'}))
    class Meta:
        model = ArticleComment
        fields = ("content",)

class ArtistPostForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = (
            "song_artist_name", 
            "song_genre", 
            "artist_song", 
            "artist_genre", 
            "song_title", 
            "artist_image", 
            "artist_profile"
        )

class ArtistSongPost(forms.ModelForm):
    class Meta:
        model = Artist
        fields = (
            "song_title",
            "song_genre",
            "artist_song",
            "artist_profile",
    )

class SongPostForm(forms.ModelForm):
    class Meta:
        model = CreateSong
        fields = ( 
            # "song_artist_name_create", 
            "song_genre_create", 
            "artist_song_create", 
            "artist_genre_create",
            "artist_song_title_create",
            # "artist_image_create",
            "artist_profile_create",
        )
