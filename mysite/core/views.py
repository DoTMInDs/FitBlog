from django.shortcuts import render,redirect, get_object_or_404
from blog.models import PostModel,ArticlePostModel
from blog.forms import CommentForm,ArticleCommentForm,ArtistPostForm,AlbumForm,SongUploadForm
from django.db.models import Q
from .models import Artist,Album,SportsModel

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
    form = ArtistPostForm()    

    if request.method == "POST":
        form = ArtistPostForm(request.POST, request.FILES)        
        if form.is_valid() :
            # instance = form.save(commit=False)
            # instance.artist_name = request.user
            # instance.save()
            form.save()            
            return redirect('music-page')
    else:
        form = ArtistPostForm()

    context = {
        "artist_uploads": artist_uploads,
        "form": form,
        
    }
    return render(request, 'core/music.html', context)

def AfricaPage(request):
    return render(request, 'core/africa.html')

@login_required
def ArtistDetailPage(request, artist_id):
    artist_uploads = get_object_or_404(Artist, id=artist_id)
    
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
                song.save()
                return redirect('artist-detail', artist_id=artist_uploads.id)
    else:
        album_form = AlbumForm()
        song_form = SongUploadForm()

    context = {
        'artist_uploads': artist_uploads,
        'album_form': album_form,
        'song_form': song_form,
        'albums': artist_uploads.albums.all(),
        'songs': artist_uploads.songs.all(),
    }
    return render(request, 'artists/artist_detail.html', context)

def SportDetailPage(request, pk):
    posts = SportsModel.objects.get(id=pk)
    post_mod = PostModel.objects.get(id=pk)

    context = {
        'posts': posts,
        'post_mod': post_mod,
    }
    return render(request, 'artists/sport_detail.html', context)