import os
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import DetailsForm 
# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "turf/landingpage.html")

def addturf_view(request):
    return render(request, "registration/addturf.html")

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

