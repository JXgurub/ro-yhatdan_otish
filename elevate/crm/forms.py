from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.forms import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput




# - Create/register a user (model form)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]




# Authenticate a user(model form)



class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())










