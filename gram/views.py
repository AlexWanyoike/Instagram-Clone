from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404

# Create your views here.

def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')

def homepage(request):
    return HttpResponse('Welcome te')

def profile_page(request):
    return HttpResponse('Welcome to ')

def viewphoto(request):
    return HttpResponse('Wel Tribune')

def sign_up(request):
    return HttpResponse('Welcoibune')

def login_user(request):
    return HttpResponse('WelcoTribune')

def create_post(request):
    return HttpResponse('Welcoibune')

def comments(request):
    return HttpResponse('Welcoibune')


