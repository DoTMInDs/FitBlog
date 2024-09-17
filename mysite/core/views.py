from django.shortcuts import render

# Create your views here.
def NewsPage(request):
    return render(request, 'core/news.html')

def SportsPage(request):
    return render(request, 'core/sports.html')

def  BusinessPage(request):
    return render(request, 'core/business.html')

def OpinionsPage(request):
    return render(request, 'core/opinions.html')

def GhanawebPage(request):
    return render(request, 'core/ghanaweb.html')

def entertainmentPage(request):
    return render(request, 'core/entertainment.html')

def AfricaPage(request):
    return render(request, 'core/africa.html')