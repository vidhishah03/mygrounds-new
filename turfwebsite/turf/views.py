import os
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
from .models import *
from django.contrib import messages
# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "turf/landingpage.html")

def addturf_view(request):
    return render(request, "registration/addturf.html")

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

<<<<<<< HEAD
   
# Create your views here. 
def detailsform_view(request): 
    form = TurfForm()
    if request.method == 'POST':
        form = TurfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application sent successfully' , extra_tags='alert')
            return redirect('home')
    return render(request, 'registration/turfdetailsform.html', {'form': form})
    


=======
>>>>>>> 8e9825259cc302673e48f2e79be78839c36b8103
