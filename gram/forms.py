from django import forms
from .models import Profile , Comment , Image , Follow , NewsLetterRecipients
#from django from forms

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

# class NewArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         exclude = ['editor', 'pub_date']
#         widgets = {
#             'tags': forms.CheckboxSelectMultiple(),
#         }