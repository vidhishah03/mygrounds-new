from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm


class TurfForm(forms.ModelForm):

    class Meta:
        model = Turf_List
        fields = ['name', 'address', 'image', 'has_refreshments', 'has_parking',
                    'has_first_aid', 'events',  'num_5v5_turfs', 'price_per_hour_5v5_weekdays',
                    'weekdays_turf_opening_time','weekdays_turf_closing_time','price_per_hour_5v5_weekends',
                    'weekends_turf_opening_time','weekends_turf_closing_time']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'emailid', 'message']


class MyAccountForm(UserChangeForm):
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class passwordchangeForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['image', 'message']
