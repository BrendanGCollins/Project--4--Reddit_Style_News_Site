from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Custom form for registering a new user
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add an email field to the default form

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Fields for the registration form