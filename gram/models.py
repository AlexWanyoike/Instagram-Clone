import datetime as dt
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
# class Create(models.Model):
#     full_name = models.CharField(max_length =30)
#     user_name = models.CharField(max_length =30)
#     email = models.EmailField()
#     confirm_email = models.EmailField()
#     #phone_number = models.CharField(max_length = 10,blank =True)

#     def __str__(self):
#         return self.full_name

#     def save_editor(self):
#         self.save()

#     class Meta:
#         #Defines the fields and class you have.
#         ordering = ['full_name']

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Newpost(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    url = models.CharField(max_length=80)
    profile_info = models.TextField(max_length=150)
    created = models.DateField(auto_now_add=True)
    favorites = models.ManyToManyField(Post)
    tags = models.ManyToManyField(tags)
    picture = models.ImageField(upload_to='media/', blank=True)


    
    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news

    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

    