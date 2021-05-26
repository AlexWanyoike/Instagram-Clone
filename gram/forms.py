from django import forms
from .models import Profile , Comment , Image , Follow  
from django import forms
#from .forms import NewsLetterForm, CreatePostForm , UserUpdateForm, ProfileUpdateForm

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'date_posted ' , 'likes', 'user']
   
