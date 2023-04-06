from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add Article", 'url_name': 'add_page'},
        {'title': "Feedback", 'url_name': 'contact'},
        {'title': "Sign in", 'url_name': 'login'}
        ]
def index(request):
    posts = AI.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Main Page',
        'cat_selected': 0,
    }

    return render(request, 'ai/index.html', context=context)

def about(request):
    return render(request, 'ai/about.html', {'menu': menu, 'title': 'Something about this site'})

def addpage(request):
    return HttpResponse("Add Article")

def contact(request):
    return HttpResponse("Feedback")

def login(request):
    return HttpResponse("Sign in")

def  pageNotFound (request, exception):
    return HttpResponseNotFound("<h1>This page does not exist</h1>")

def show_post(request, post_id):
    return HttpResponse(f"Show Article with ID = {post_id}")


def show_category(request, cat_id):
    posts = AI.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Show by Category',
        'cat_selected': cat_id,
    }

    return render(request, 'ai/index.html', context=context)