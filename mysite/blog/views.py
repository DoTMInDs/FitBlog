from django.shortcuts import render,redirect # type: ignore
from django.contrib.auth.decorators import login_required

from .models import PostModel,ArticlePostModel
from.forms import CommentForm,ArticleCommentForm
from django.db.models import Q

from django.core.paginator import Paginator

def HomePageView(request):
    posts = PostModel.objects.all()
    articles = ArticlePostModel.objects.all()
    
    filter_query = request.GET.get('search') if request.GET.get('search') != None else ''
    articles = ArticlePostModel.objects.filter(
        Q(title__icontains=filter_query) |
        Q(author__username__icontains=filter_query) |
        Q(sub_title__icontains=filter_query) |
        Q(article_content__icontains=filter_query)
    )
    
    
     # Pagination for articles
    article_paginator = Paginator(articles, 2)  # Show 5 articles per page
    article_page_number = request.GET.get('article_page')
    article_page_obj = article_paginator.get_page(article_page_number)

   
    context = {
        'article_page_obj': article_page_obj,
        'posts': posts,
    }
    return render(request, 'home.html', context)

@login_required
def post_detail(request, pk):
    articles = ArticlePostModel.objects.get(id=pk)
    if request.method == 'POST':
        c_form = ArticleCommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = request.user
            instance.article = articles
            instance.save()
            return redirect('blog-post-detail', pk=articles.id)
    else:
        c_form = ArticleCommentForm()
    context = {
        'articles': articles,
        'c_form': c_form,
    }
    return render(request, 'blog/post_detail.html', context)

@login_required
def postmodel_detail(request, pk):
    post_mod = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.post_user = request.user
            instance.post_com = post_mod
            instance.save()
            return redirect('blog-postmodel-detail', pk=post_mod.id)
    else:
        c_form = CommentForm()
    context = {
        'post_mod': post_mod,
        'c_form': c_form,
    }
    return render(request, 'blog/postmodel_detail.html', context)
