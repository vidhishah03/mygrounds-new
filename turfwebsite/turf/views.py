import os
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
from .models import *
from django.contrib import messages
from .filters import Turf_ListFilter
# Create your views here.


def home_view(request, *args, **kwargs):
    cform = ContactForm()
    if request.method == 'POST':
        cform = ContactForm(request.POST)
        if cform.is_valid():
            cform.save()
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
    myFilter = Turf_ListFilter(request.GET, queryset=display)
    display = myFilter.qs
    context = {'display': display, 'myFilter': myFilter}
    return render(request, 'registration/display.html', context)

def show_contacts(request):
    Contact_show = Contact.objects.all()
    return render(request, 'turf/contact_show.html', {'Contact_show': Contact_show})


class myaccountview(generic.UpdateView):
    form_class = MyAccountForm
    success_url = reverse_lazy('myaccount')
    template_name = 'registration/myaccount.html'



    def get_object(self):
        return self.request.user
   




class passwordchangeview(PasswordChangeView):
    form_class = passwordchangeForm
    success_url = reverse_lazy('myaccount')
    template_name = 'registration/changepassword.html'


# Create your views here.
def feedbackview(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Thank you for your feedback :)', extra_tags='alert')
            return redirect('home')
    return render(request, 'turf/gallery.html', {'form': form})

     
    
def user_posts( request):   
    logged_in_user = request.user
    logged_in_user_posts = Turf_List.objects.filter(owner=logged_in_user)
    return render(request, 'registration/myaccountextend.html', {'turfs': logged_in_user_posts})


