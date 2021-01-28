from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

class TurfForm(forms.ModelForm):

    class Meta:
        model = Turf_List
        fields = ['name', 'address', 'image', 'facilities',
                  'emergency', 'events',  'num_5v5', 'price_per_hour_5v5', 'num_7v7', 'price_per_hour_7v7',  'num_7v7_5v5',  'num_12v12', 'price_per_hour_12v12']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'emailid', 'message']

class MyAccountForm(UserChangeForm):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class passwordchangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']