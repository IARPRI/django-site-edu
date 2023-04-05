from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ["About", "Add Article", "Feedback", "Sign in"]
def index(request):
    posts = AI.objects.all()
    return render(request, 'ai/index.html', {'posts': posts, 'menu': menu, 'title': 'Main Page'})

def about(request):
    return render(request, 'ai/about.html', {'menu': menu, 'title': 'Something about this site'})

def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Articles by category</h1><p>{catid}</p>")

def  archive (request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Archive by year</h1><p>{year}</p>")

def  pageNotFound (request, exception):
    return HttpResponseNotFound("<h1>This page does not exist</h1>")