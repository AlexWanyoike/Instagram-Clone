import datetime as dt
from django.db import models
from django.contrib.auth.models import User 
from tinymce.models import HTMLField
from django.db.models.base import Model

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='media/')
    bio = models.TextField(blank=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)  

    def __str__(self) -> str:
        return self.user.username

    @classmethod
    def search_user(cls,username):
        return User.objects.filter(username = username)     


class Image(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/')
    caption = models.TextField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE )
    likes = models.ManyToManyField(Profile, related_name="posts")

    def __str__(self) -> str:
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

    @classmethod
    def get_profile_images(cls,profile):
        return cls.objects.filter(profile = profile)

    # class Meta:
    #     ordering = ['-post_date']



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
    name = models.CharField(max_length = 30)
    email = models.EmailField()



# # Create your models here.
# # class Create(models.Model):
# #     full_name = models.CharField(max_length =30)
# #     user_name = models.CharField(max_length =30)
# #     email = models.EmailField()
# #     confirm_email = models.EmailField()
# #     #phone_number = models.CharField(max_length = 10,blank =True)

# #     def __str__(self):
# #         return self.full_name

# #     def save_editor(self):
# #         self.save()

# #     class Meta:
# #         #Defines the fields and class you have.
# #         ordering = ['full_name']

# class tags(models.Model):
#     name = models.CharField(max_length =30)

#     def __str__(self):
#         return self.name


# class Newpost(models.Model):

#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     full_name = models.CharField(max_length=50)
#     location = models.CharField(max_length=50)
#     url = models.CharField(max_length=80)
#     profile_info = models.TextField(max_length=150)
#     created = models.DateField(auto_now_add=True)
#     #favorites = models.ManyToManyField(Post)
#     tags = models.ManyToManyField(tags)
#     picture = models.ImageField(upload_to='media/', blank=True)


    
#     @classmethod
#     def todays_news(cls):
#         today = dt.date.today()
#         news = cls.objects.filter(pub_date__date = today)
#         return news

#     @classmethod
#     def days_news(cls,date):
#         news = cls.objects.filter(pub_date__date = date)
#         return news

#     @classmethod
#     def search_by_title(cls,search_term):
#         news = cls.objects.filter(title__icontains=search_term)
#         return news

# class NewsLetterRecipients(models.Model):
#     name = models.CharField(max_length = 30)
#     email = models.EmailField()

    