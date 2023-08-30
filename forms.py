from django import forms
from eapp.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class CustomUserForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}))
    phone_number=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Mobile Number'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password '}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Confirm Password'}))
   
    class Meta: 
        model=CustomUser
        fields=["first_name","last_name","username","email","phone_number","password1","password2"]