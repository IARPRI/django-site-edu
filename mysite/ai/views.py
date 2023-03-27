from django.http import HttpResponse
from django.shortcuts import render

def index(request): #HttpRequest
    return HttpResponse("ai app page")

def  categories (request):
    return HttpResponse("<h1>Articles by category</h1>")