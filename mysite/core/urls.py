from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.NewsPage, name='news-page' ),
    path('sports/', views.SportsPage, name='sports-page' ),
    path('business/', views.BusinessPage, name='business-page' ),
    path('opinions/', views.OpinionsPage, name='opinions-page' ),
    path('ghanaweb/', views.GhanawebPage, name='ghanaweb-page' ),
    path('music/', views.MusicPage, name='music-page' ),
    path('africa/', views.AfricaPage, name='africa-page' ),

    path('all_artist/', views.all_artist, name='all-artist' ),
    path('all_album/', views.all_album, name='all-album' ),
    path('album_detail/<int:album_id>/', views.AlbumDetail, name='album-detail' ),
    path('artist_detail/<int:artist_id>/', views.ArtistDetailPage, name='artist-detail' ),
    path('sport_detail/<int:pk>/', views.SportDetailPage, name='sport-detail' ),
]
