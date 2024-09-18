from django.shortcuts import render,redirect # type: ignore
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.contrib.auth import  logout # type: ignore
from django.contrib import auth, messages # type: ignore

from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm,UserPostForm,PostEditForm

from blog.models import ArticlePostModel
# from django.core.paginator import Paginator



# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('user-dashboard')
        else:
            messages.error(request, "Please input a valid username and password")
       
    return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    return render(request, 'users/logout.html')
    

def reset_password(request):
    return render(request, 'users/reset_password.html')


def sign_up(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        #     print("form is valid")
        # else:
        #     print(form.errors)

    context = {'form':form}
    return render(request, 'users/sign_up.html', context)


def profile(request):

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)

def user_dashboard(request):
    articles = ArticlePostModel.objects.all()
    user_post_form = UserPostForm()

    if request.method == "POST":
        user_post_form = UserPostForm(request.POST, request.FILES)
        if user_post_form.is_valid():
            instance = user_post_form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('user-dashboard')
        else:
            user_post_form = UserPostForm()
    context = {
        'articles': articles,
        'user_post_form': user_post_form,
    }
    return render(request, 'dashboard/dashboard.html',context)

def user_dashboard_edit(request, pk):
    articles = ArticlePostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=articles)
        if form.is_valid():
            form.save()
            return redirect('user-dashboard')
    else:
        form = PostEditForm(instance=articles)
   
    context = {
        'articles': articles,
        'form': form,
    }
    return render(request, 'dashboard/user_dashboard_edit.html', context)

def user_post_delete(request, pk):
    articles = ArticlePostModel.objects.get(id=pk)
    if request.method == 'POST':
        articles.delete()
        return redirect('home')
    context = {
        'articles': articles,
    }
    return render(request, 'dashboard/user_post_delete.html', context)