from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse ,Http404

# Create your views here.

def base(request):
    return render(request , 'base.html')

def home(request):
    return render(request ,'home.html')

def user_profile(request):
    return render(request ,'profile.html' )

def viewphoto(request):
    return render(request ,'viewphoto.html')

def sign_up(request):
    return render(request ,'signup.html')

def login_user(request):
    return render(request ,'login.html')

def create_post(request):
    return render(request ,'create_post.html')

def comments(request):
    return render(request ,'comments.html')

def ignore_nav(request):
    return render(request ,'instagram-nav.html')


