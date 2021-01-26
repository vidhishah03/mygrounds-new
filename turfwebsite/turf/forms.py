from django import forms
from .models import *


class TurfForm(forms.ModelForm):

    class Meta:
        model = Turf_List
        fields = ['name', 'address', 'image', 'facilities',
                  'emergency', 'events',  'num_5v5', 'price_per_hour_5v5', 'num_7v7', 'price_per_hour_7v7',  'num_7v7_5v5',  'num_12v12', 'price_per_hour_12v12']
