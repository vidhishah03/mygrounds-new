import os
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, os.path.join("turf", "index.html"), {})
