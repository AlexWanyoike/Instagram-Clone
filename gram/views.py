from django.shortcuts import render , redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Image , Profile , Comment , Follow
#from .forms import CreatePostForm, NewsLetterForm
from django import forms
from django.urls import reverse
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# Create your views here.

def main(request):
    

    create_post = request.GET.get('Profile')
    if create_post  == None:
        photo = Image.objects.all()
    else:
        photo = Photo.objects.filter(create_post__name=create_post)
    create_post = Image.objects.all()

    username = request.GET.get('Profile')
    username = Profile.objects.all()

    comment = request.GET.get('Comment')
    comment = Comment.objects.all()

    context = {'photo': photo , 'username': username}

    return render(request , 'main.html', context)


@login_required(login_url='/registration/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = current_user
            post.save()
        return redirect('main')

    else:
        form = CreatePostForm()
    return render(request, 'main.html', {"form": form})


# def comment(request):
#     print("AJAX is working")

#     comment = request.GET.get('Comment')
#     image = request.GET.get('Image')
#     username = request.user

#     comment = Comment(comment=comment,image=image,username=username)
#     comment.save()

#     recent_comment= f'{Comment.objects.all().last().comment}'
#     recent_comment_user = f'{Comment.objects.all().last().username}'
#     data= {
#         'recent_comment': recent_comment,
#         'recent_comment_user':recent_comment_user
#     }

#     return JsonResponse(data)

def base(request):
    return render(request , 'base.html')

def home(request):
    return render(request ,'home.html')

def user_profile(request):
    return render(request ,'profile.html' )

def viewphoto(request):
    return render(request ,'viewphoto.html')

def sign_up(request):
    return render(request ,'registration/signup.html')

def login(request):
    return render(request ,'registration/login.html')

def create_post(request):
    return render(request ,'create_post.html')

def comments(request):

    return render(request ,'comments.html')

def ignore_nav(request):
    return render(request ,'instagram-nav.html')

def edit_profile(request):
    return render(request ,'edit_profile.html')

def change_password(request):
    return render(request ,'change_password.html')


class UserRegistration(generic.CreateView):
    form_class = UserCreationForm
    success = reverse_lazy('login')