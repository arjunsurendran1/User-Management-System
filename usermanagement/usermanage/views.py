from django.shortcuts import render, redirect
#import requests
#from bs4 import BeautifulSoup
import datetime
from . models import *
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import make_password
# Create your views here.


def home(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'home.html')


def registeration(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')
