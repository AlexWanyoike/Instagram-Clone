from django.urls import path , re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.main,name = 'main'),
    path('profile/',views.user_profile,name = 'profile'),
    path('viewphoto//<str:pk>/',views.viewphoto,name = 'viewphoto'),
    path('create_post/',views.create_post,name = 'create_post'),
    path('comments/',views.comments,name = 'comments'),
    #path('nav-gram/',views.ignore_nav,name = 'nav-gram'),
    path('edit_profile/',views.edit_profile,name = 'edit_profile'),
    path('change_password/',views.change_password,name = 'change_password'),
    #re_path('new/article$', views.new_article, name='new-article')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)