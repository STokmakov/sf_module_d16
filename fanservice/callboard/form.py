from django import forms
from .models import Advert, UserResponse
class AdvertForm(forms.ModelForm):
   class Meta:
       model = Advert
       fields = [
           'user',
           'subject',
           'category',
           'description',
       ]
class UserResponseForm(forms.ModelForm):
   class Meta:
       model = UserResponse
       fields = [
           'user',
           'subject',
           'description',
           'advert',
       ]
