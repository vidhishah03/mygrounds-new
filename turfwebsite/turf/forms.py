from django import forms 
<<<<<<< HEAD

from .models import *
class TurfForm(forms.ModelForm):
    class Meta:
        model = Turf_List
        fields = ['name', 'address', 'image', 'facilities', 'near_by_turf', 'emergency', 'events']
=======
   
# creating a form  
class DetailsForm(forms.Form): 
   
    first_name = forms.CharField(max_length = 50) 
    last_name = forms.CharField(max_length = 50)
    phone_number = forms.IntegerField
    turf_name = forms.CharField(max_length = 50)
    turf_address = forms.CharField(max_length = 200)
    
>>>>>>> 8e9825259cc302673e48f2e79be78839c36b8103

     