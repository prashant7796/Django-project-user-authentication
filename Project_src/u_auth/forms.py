from cProfile import label
from contextlib import nullcontext
from distutils.command.upload import upload
from email.policy import default
from random import choices
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.forms import Form


a_type = (
    ("1", "Doctor"),
    ("2", "Patient"),
)
class CreateUserForm(UserCreationForm):
    account_type = forms.ChoiceField(label='Account Type: ', choices=a_type)
    first_name = forms.CharField(label='First Name: ', min_length=3, max_length=20)
    last_name = forms.CharField(label='Last Name: ', min_length=3, max_length=20)
    profile_pic = forms.URLField(label='Profile Picture: ')
    username = forms.CharField(label='Username: ', min_length=4, max_length=20)
    email = forms.EmailField(label='Email Id: ')
    password1 = forms.CharField(label='Password: ', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirm password: ' , widget=forms.PasswordInput) 
    address = forms.CharField(label='Address: ', min_length=5, max_length=100)
