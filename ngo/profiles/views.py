"""Profile views."""

# Django
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Models.
from .models import Profile


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    login_url = "users:login"
    model = Profile
    fields = "__all__"
    template_name = "profiles/update.html"
    success_url = reverse_lazy("home")


# Create your views here.
