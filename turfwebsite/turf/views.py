import os
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, os.path.join("turf", "index.html"), {})
