import os
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
from .models import *
from django.contrib import messages
# Create your views here.


def home_view(request, *args, **kwargs):
    cform = ContactForm()
    if request.method == 'POST':
        cform = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Application sent successfully', extra_tags='alert')
            return redirect('home')
    return render(request, 'turf/landingpage.html', {'cform': cform})


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# Create your views here.
def detailsform_view(request):
    form = TurfForm()
    if request.method == 'POST':
        form = TurfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Application sent successfully', extra_tags='alert')
            return redirect('home')
    return render(request, 'registration/turfdetailsform.html', {'form': form})


def show_turf(request):
    display = Turf_List.objects.all()
    return render(request, 'registration/display.html', {'display': display})


def addturf_view(request):
    return render(request, "registration/addturf.html")


def show_contacts(request):
    Contact_show = Contact.objects.all()
    return render(request, 'turf/contact_show.html', {'Contact_show': Contact_show})


def myaccount_view(request):
    form = accountform()
    if request.method == 'POST':
        form = accountform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Details saved successfully', extra_tags='alert')
            return redirect('myaccount')
    return render(request, 'registration/myaccount.html', {'form': form})
