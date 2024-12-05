from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World!")

def home(request):
    # return HttpResponse("Welcome to the Home Page!")
    # return render(request, "appweb/home.html")  # Include the app folder in the path
    return render(request, "appweb/home.html")