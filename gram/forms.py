from django import forms
from .models import Profile , Comment , Image , Follow , NewsLetterRecipients
#from django from forms

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

# class CreatePostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['editor', 'pub_date']
#         widgets = {
#             'tags': forms.CheckboxSelectMultiple(),
#         }