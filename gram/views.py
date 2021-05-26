from django.shortcuts import render , redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import CreatePostForm, NewsLetterForm
from .models import Image , Profile , Comment , Follow
from django import forms
from .forms import NewsLetterForm, CreatePostForm , UserUpdateForm, ProfileUpdateForm
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


# Commenting on a Post 
@login_required
def comment(request, image_id):
    photo = Image.objects.get(pk=photo_id)
    content = request.GET.get("comment")
    user = request.user
    comments = Comment.objects.all()
    component = {'photo': photo , 'comments': comments}
    comment= Comment(photo = photo, content = content, user=user)
    comment.save_comment()
    return render(request , 'comments.html', component)
    # return redirect('main')

def user_profile(request):
    return render(request ,'profile.html' )

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

# class UserRegistration(generic.CreateView):
#     form_class = UserCreationForm
#     success = reverse_lazy('login')


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

# def sign_up(request):
#     return render(request ,'signup.html')

# def login(request):
#     return render(request ,'login.html')


def comments(request):
    return render(request ,'comments.html')


