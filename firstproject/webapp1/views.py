from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

# Create your views here.
def home(request):
    return render(request, 'webapp1/home.html')