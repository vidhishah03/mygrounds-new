from django import forms 

from .models import *
class TurfForm(forms.ModelForm):
    class Meta:
        model = Turf_List
        fields = ['name', 'address', 'image', 'facilities', 'near_by_turf', 'emergency', 'events']

     