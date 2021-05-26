import datetime as dt
from django.db import models
from django.contrib.auth.models import User 
from tinymce.models import HTMLField
from django.db.models.base import Model

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE )
    name = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(upload_to='media/', default='')
    bio = models.TextField(blank=True, default='')
    followers = models.IntegerField(default=0 )
    following = models.IntegerField(default=0 )  

    def __str__(self):
        return self.user.username

    def get_user_by_profile(cls, username):
        profile = Profile.cls.objects.filter(user__username__contains = username) 
        return profile

    @classmethod
    def search_user(cls,username):
        return User.objects.filter(username = username)     


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True)
    name = models.CharField(max_length=30 , blank=True )
    image = models.ImageField(upload_to='media/')
    caption = models.TextField(max_length=400, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE , null=True)
    likes = models.ManyToManyField(Profile, related_name="posts")

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()

    def like_count(self):
        return self.likes.count()

    def get_image_by_user(cls, username):
        images = Image.cls.objects.filter(user__username__contains = username) 
        return images

    @classmethod
    def get_profile_images(cls,profile):
        return cls.objects.filter(profile = profile)

    class Meta:
        ordering = ['-date_posted']


class Comment(models.Model):
    content = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.content

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_image_comments(cls,image):
        return cls.objects.filter(image =image)

    class Meta:
        ordering = ['-post_date']

class Follow(models.Model): 
    posted = models.DateTimeField(auto_now_add=True)
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_followed')
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_following')

    def __str__(self):
        return self.pk 

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30, default='')
    email = models.EmailField()

