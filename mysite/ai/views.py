from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request): #HttpRequest
    return HttpResponse("ai app page")

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