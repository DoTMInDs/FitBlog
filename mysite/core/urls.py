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

    path('artist_detail/<int:artist_id>/', views.ArtistDetailPage, name='artist-detail' ),
    path('sport_detail/<int:pk>/', views.SportDetailPage, name='sport-detail' ),
]
