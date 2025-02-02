from django.shortcuts import render,redirect, get_object_or_404
from blog.models import PostModel,ArticlePostModel
from blog.forms import CommentForm,ArticleCommentForm,ArtistPostForm,AlbumForm,SongUploadForm
from django.db.models import Q
from .models import Artist,Album,SportsModel,Song

from django.contrib.auth.decorators import login_required
# from django.views.generic.list import ListView

# from django.core.paginator import Paginator


# Create your views here.
# class NewsListView(ListView):
#     paginate_by = 2
#     model = ArticlePostModel
#     template_name = 'core/news.html'
#     def listing(request):        
#         posts = PostModel.objects.all()
#         articles = ArticlePostModel.objects.all()
#         paginator = Paginator(articles, 5)  # Show 25 contacts per page.

#         page_number = request.GET.get("page")
#         page_obj = paginator.get_page(page_number)
#         context = {
#             'articles': articles,
#             'posts': posts,
#             'page_obj': page_obj,
#         }
#         return render(request, 'core/news.html', context)

@login_required
def NewsPage(request):
    posts = PostModel.objects.all()
    articles = ArticlePostModel.objects.all()
    
    filter_query = request.GET.get('search') if request.GET.get('search') != None else ''
    articles = ArticlePostModel.objects.filter(
        Q(title__icontains=filter_query) |
        Q(author__username__icontains=filter_query) |
        Q(sub_title__icontains=filter_query) 
    )

    context = {
        'articles': articles,
        'posts': posts,
    }
    return render(request, 'core/news.html', context)

def SportsPage(request):
    posts = SportsModel.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'core/sports.html',context)

def  BusinessPage(request):
    return render(request, 'core/business.html')

def OpinionsPage(request):
    return render(request, 'core/opinions.html')

def GhanawebPage(request):
    return render(request, 'core/ghanaweb.html')

@login_required
def MusicPage(request):
    artist_uploads = Artist.objects.all()
    albums = Album.objects.all()
    form = ArtistPostForm()   
    a_form = AlbumForm() 

    if request.method == "POST":
        if 'form' in request.POST:
            form = ArtistPostForm(request.POST, request.FILES)        
            if form.is_valid() :
                form.save()            
                return redirect('music-page')
        elif 'a_form' in request.POST:
            a_form = AlbumForm(request.POST, request.FILES)
            if a_form.is_valid():
                a_form.save()
                return redirect('music-page')
        
    else:
        form = ArtistPostForm()
        a_form = AlbumForm() 

    context = {
        "artist_uploads": artist_uploads,
        "albums": albums,
        "form": form,
        "a_form": a_form,
        
    }
    return render(request, 'core/music.html', context)

def AfricaPage(request):
    return render(request, 'core/africa.html')

@login_required
def ArtistDetailPage(request, artist_id):
    artist_uploads = get_object_or_404(Artist, id=artist_id)
    songs = Song.objects.filter(artist=artist_uploads)
    
    album_form = AlbumForm()
    song_form = SongUploadForm()
   
    if request.method == "POST":
        if 'album_form' in request.POST:
            album_form = AlbumForm(request.POST, request.FILES)
            if album_form.is_valid():
                album = album_form.save(commit=False)
                album.artist = artist_uploads
                album.save()
                return redirect('artist-detail', artist_id=artist_uploads.id)
        elif 'song_form' in request.POST:
            song_form = SongUploadForm(request.POST, request.FILES)
            if song_form.is_valid():
                song = song_form.save(commit=False)
                song.artist = artist_uploads
                album_id = request.POST.get('album')
                if album_id:
                    song.album = get_object_or_404(Album, id=album_id)
                song.save()
                return redirect('artist-detail', artist_id=artist_uploads.id)

    context = {
        "artist_uploads": artist_uploads,
        "songs": songs,
        'album_form': album_form,
        'song_form': song_form,
    }
    return render(request, 'artists/artist_detail.html', context)


@login_required
def all_artist(request):
    artist_uploads = Artist.objects.all()

    context = {
        "artist_uploads": artist_uploads,
    }
    return render(request, 'artists/all_artist.html', context)
    
@login_required
def all_album(request):
    albums = Album.objects.all()

    context = {
        "albums": albums,
    }
    return render(request, 'artists/all_album.html', context)

@login_required
def AlbumDetail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    
    song_form = SongUploadForm()
    
    if request.method == "POST":
        if 'song_form' in request.POST:
            song_form = SongUploadForm(request.POST, request.FILES)
            if song_form.is_valid():
                song = song_form.save(commit=False)
                song.album = album
                song.artist = album.artist
                song.save()
                return redirect('album-detail', album_id=album.id)
    else:
        song_form = SongUploadForm()

    context = {
        "album": album,
        "song_form": song_form,
        'songs': album.songs.all(),
    }
    return render(request, 'artists/album_details.html', context)
    

def SportDetailPage(request, pk):
    posts = SportsModel.objects.get(id=pk)
    post_mod = PostModel.objects.get(id=pk)

    context = {
        'posts': posts,
        'post_mod': post_mod,
    }
    return render(request, 'artists/sport_detail.html', context)