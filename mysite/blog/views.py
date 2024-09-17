from django.shortcuts import render # type: ignore
from .models import PostModel,ArticlePostModel


# from django.http import HttpResponse
# from django.views.generic.base import TemplateView
# from .models import BlogProfile

def HomePageView(request):
    posts = PostModel.objects.all()
    articles = ArticlePostModel.objects.all()
    context = {
        'posts': posts,
        'articles': articles
    }
    return render(request, 'home.html', context)

def post_detail(request, pk):
    articles = ArticlePostModel.objects.get(id=pk)
    context = {
        'articles': articles
    }
    return render(request, 'blog/post_detail.html', context)

def postmodel_detail(request, pk):
    post_mod = PostModel.objects.get(id=pk)
    context = {
        'post_mod': post_mod
    }
    return render(request, 'blog/postmodel_detail.html', context)
