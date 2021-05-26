from django.shortcuts import render , redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import CreatePostForm, NewsLetterForm
from .models import Image , Profile , Comment , Follow
from django import forms
from .forms import NewsLetterForm, CreatePostForm
from django.urls import reverse
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# Create your views here.

def main(request):
    image = Image.objects.all()
    comments = Comment.objects.all()

    context = {'image': image ,'comments': comments}

    return render(request , 'main.html', context)

@login_required
def user_profile(request, username):

    date = dt.date.today()
    images = Image.get_image_by_user(username)
    profile = Profile.get_profile(username)

    context = {'images': images ,'profile': profile, 'date': date}

    return render(request ,'profile.html' , context )

def viewphoto(request):
    return render(request ,'viewphoto.html')

# Creating a post
@login_required
def create_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreatePostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return HttpResponseRedirect('/')
           
    else:
        form = CreatePostForm()
        return render(request, 'create_post.html', {"form": form})


def ignore_nav(request):
    return render(request ,'instagram-nav.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('edit_profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request ,'edit_profile.html' , context)

def change_password(request):
    return render(request ,'change_password.html')

@login_required
def email(request):
    current_user = request.user
    name = current_user.username
    email = current_user.email
    print ('email')
    send_welcome_email(name, email)
    return redirect(profile)



def comments(request):
    return render(request ,'comments.html')


