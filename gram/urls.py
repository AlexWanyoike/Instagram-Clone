from django.urls import path , re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.base,name = 'welcome'),
    path('main/',views.main,name = 'welcome'),
    path('home/',views.home,name = 'welcome'),
    path('profile/',views.user_profile,name = 'welcome'),
    path('viewphoto/',views.viewphoto,name = 'welcome'),
    path('sign_up/',views.sign_up,name = 'welcome'),
    path('login_user/',views.login_user,name = 'welcome'),
    path('create_post/',views.create_post,name = 'welcome'),
    path('comments/',views.comments,name = 'welcome'),
    path('nav-gram/',views.ignore_nav,name = 'welcome'),
    path('edit_profile/',views.edit_profile,name = 'welcome'),
    path('change_password/',views.change_password,name = 'welcome'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)