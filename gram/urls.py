from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('homepage/',views.homepage,name = 'welcome'),
    path('profile_page/',views.profile_page,name = 'welcome'),
    path('viewphoto/',views.viewphoto,name = 'welcome'),
    path('sign_up/',views.sign_up,name = 'welcome'),
    path('login_user/',views.login_user,name = 'welcome'),
    path('create_post/',views.create_post,name = 'welcome'),
    path('comments/',views.comments,name = 'welcome'),
]