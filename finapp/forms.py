from django import forms
from django.contrib.auth.models import User

from .models import Product
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField


class AddProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','category','image','descriptions','info','profit','link']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-input'}),
            'descriptions':forms.Textarea(attrs={'cols':60,'rows':10}),
            'info':forms.Textarea(attrs={'cols':60,'rows':10}),

        }


class UserRegisterForm(UserCreationForm):

    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

class ContactForm(forms.Form):
    name=forms.CharField(label='Имя',max_length=155)
    email=forms.EmailField()
    text=forms.CharField(label='Текст',widget=forms.Textarea(attrs={'cols':60,'rows':10}))
    captcha=CaptchaField()