from django.urls import reverse_lazy
from certifi import where
from django.views.generic import View
import logging
from django. shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError, send_mass_mail
from django.contrib.auth.models import User
from .form import SignUpForm
import ssl
import certifi
from django.db import IntegrityError
import smtplib


ssl_context = ssl.create_default_context(cafile=certifi.where())

logger = logging.getLogger(__name__)


class SignUpView(View):
    template_name = "signup.html"

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()
            except IntegrityError as e:
                if 'UNIQUE constraint failed' in str(e):
                    form.add_error(
                        'username', 'This username is already taken.')
                else:
                    form.add_error(
                        None, 'An unexpected error occurred. Please try again.')
                return render(request, self.template_name, {"form": form})

            try:
                self.send_welcome_email(user)
            except Exception as e:
                logger.error(f'Error sending welcome email: {str(e)}')
                form.add_error(None, f'Error sending welcome email: {str(e)}')
                return render(request, self.template_name, {"form": form})

            return redirect(reverse_lazy('dashboard'))

        return render(request, self.template_name, {"form": form})

    def send_welcome_email(self, user):
        subject = 'Welcome to Kashmir Tourism'
        message = f'Hi {user.username}, thank you for registering.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email,]
        msg = (subject, message, email_from, recipient_list)
        send_mail(subject, message, email_from,
                  recipient_list, fail_silently=False)
