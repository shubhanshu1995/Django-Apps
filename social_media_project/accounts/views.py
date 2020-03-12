from django.shortcuts import render
from django.urls import reverse_lazy #if someone is logged in or logged out, where should they actually go 
from django.views.generic import CreateView

from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login') #After successful sign up, reverse them up to the login page
    template_name = 'accounts/signup.html'