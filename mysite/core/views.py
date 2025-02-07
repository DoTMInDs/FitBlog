from django.shortcuts import render,redirect, get_object_or_404
from blog.models import PostModel,ArticlePostModel
from blog.forms import CommentForm,ArticleCommentForm,ArtistPostForm,AlbumForm,SongUploadForm
from django.db.models import Q
from .models import Artist,Album,SportsModel,Song
from django.contrib.auth.decorators import login_required
# from django.contrib import messages

# import requests
# import logging
# from django.conf import settings

# from .forms import PaymentForm
# from .models import Payment

# logger = logging.getLogger(__name__)


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
    # query = request.GET.get('search', '')
    # if query:
    #     artist_uploads = Artist.objects.filter(Q(artist__icontains=query) | Q(artist_genre__icontains=query))
    #     albums = Album.objects.filter(Q(title__icontains=query) | Q(artist__artist__icontains=query))
    # else:
    #     artist_uploads = Artist.objects.all()
    #     albums = Album.objects.all()
    
    query = request.GET.get('search')
    if query:
        artist_uploads = Artist.objects.filter(artist__icontains=query)
        albums = Album.objects.filter(title__icontains=query)
    else:
        artist_uploads = Artist.objects.all()
        albums = Album.objects.all()
        
    form = ArtistPostForm()   
    a_form = AlbumForm() 

    if request.method == "POST":
        if 'form' in request.POST:
            form = ArtistPostForm(request.POST, request.FILES)        
            if form.is_valid() :
                artist = form.save(commit=False)
                artist.user = request.user
                artist.save()            
                return redirect('music-page')
        elif 'a_form' in request.POST:
            a_form = AlbumForm(request.POST, request.FILES)
            if a_form.is_valid():
                album = a_form.save(commit=False)
                album.user = request.user
                album.save()
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
    song_form = SongUploadForm()
    
    if request.method == "POST" and 'song_form' in request.POST:
        song_form = SongUploadForm(request.POST, request.FILES)
        if song_form.is_valid():
            song = song_form.save(commit=False)
            song.artist = artist_uploads
            song.user = request.user
            song.save()
            return redirect('artist-detail', artist_id=artist_uploads.id)

    context = {
        "artist_uploads": artist_uploads,
        "songs": songs,
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



# @login_required
# def payment_view(request):
#     if request.method == 'POST':
#         form = PaymentForm(request.POST)
#         if form.is_valid():
#             amount = form.cleaned_data['amount']
#             phone_number = form.cleaned_data['phone_number']

#             headers = {
#                 'Authorization': f'Bearer {settings.MTN_MOMO_PRIMARY_KEY}',
#                 'Ocp-Apim-Subscription-Key': settings.MTN_MOMO_API_KEY,
#                 'X-Reference-Id': settings.MTN_MOMO_API_USER_ID,
#                 'X-Target-Environment': 'sandbox',  # Use 'sandbox' for testing, 'mtncameroon' for production
#                 'Content-Type': 'application/json'
#             }

#             payload = {
#                 'amount': str(amount),
#                 'currency': 'GHS',  # Change to the appropriate currency
#                 'externalId': '123456',
#                 'payer': {
#                     'partyIdType': 'MSISDN',
#                     'partyId': phone_number
#                 },
#                 'payerMessage': 'Payment for services',
#                 'payeeNote': 'Thank you for your payment'
#             }

#             response = requests.post(f'{settings.MTN_MOMO_BASE_URL}/collection/v1_0/requesttopay', headers=headers, json=payload)

#             if response.status_code == 202:
#                 transaction_id = response.json().get('transactionId')
#                 Payment.objects.create(
#                     user=request.user,
#                     amount=amount,
#                     momo_transaction_id=transaction_id
#                 )
#                 messages.success(request, 'Payment successful!')
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Payment failed. Please try again.')
#         else:
#             messages.error(request, 'Invalid form submission.')
#     else:
#         form = PaymentForm()

#     return render(request, 'core/payment.html', {'form': form})