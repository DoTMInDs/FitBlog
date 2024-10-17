from django.shortcuts import render,redirect
from blog.models import PostModel,ArticlePostModel
from blog.forms import CommentForm,ArticleCommentForm,ArtistPostForm,SongPostForm,ArtistSongPost
from django.db.models import Q
from .models import Artist,CreateSong

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
    return render(request, 'core/sports.html')

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
def ArtistDetailPage(request, pk):
    artist_uploads = Artist.objects.get(id=pk)

    song_uploads = Artist.objects.all()
    s_form = SongPostForm()
    # song_form = ArtistSongPost()

    if request.method == "POST":
        s_form = SongPostForm(request.POST, request.FILES)
        # song_form = ArtistPostForm(request.POST, request.FILES)
        if s_form.is_valid():
            s_form.save()
            # song_form.save()
            return redirect('artist-detail', pk=artist_uploads.id)
    else:
        s_form = SongPostForm()

    context = {
        'artist_uploads': artist_uploads,
        'song_uploads': song_uploads,
        's_form': s_form,
        # "song_form": song_form,
    }
    return render(request, 'artists/artist_detail.html', context)