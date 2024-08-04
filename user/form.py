from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "email"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "col-md-6 form-control"}),
            "password": forms.PasswordInput(attrs={"class": "col-md-6 form-control"}),
            "email": forms.EmailInput(attrs={"class": "col-md-6 form-control"}),
        }
        labels = {
            "username": "Name",
            "password": "Password",
            "email": "Email ID",
        }
        help_texts = {
            "username": "Enter a title for your todo",
            "password": "Enter a description for your todo",
            "email": "Enter a description for your todo"

        }

        error_messages = {
            "username": {"required": "Name is required"},
            "password": {"required": "Password is required"},
            "email": {"required": "Email ID is required"},
        }
