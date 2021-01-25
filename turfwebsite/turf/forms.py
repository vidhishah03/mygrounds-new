from django import forms 
   
# creating a form  
class DetailsForm(forms.Form): 
   
    first_name = forms.CharField(max_length = 50) 
    last_name = forms.CharField(max_length = 50)
    phone_number = forms.IntegerField
    turf_name = forms.CharField(max_length = 50)
    turf_address = forms.CharField(max_length = 200)
    

     