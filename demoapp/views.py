from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    content = "<html><body><h2>Welcome to little lemon</h2></body></html>"
    return HttpResponse(content)

def index(request):
    return HttpResponse("Hello world")

def Items(request):
    return HttpResponse("THis is shopping Items")