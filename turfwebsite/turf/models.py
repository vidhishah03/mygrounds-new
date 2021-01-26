from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Turf_List(models.Model):
    name = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=500, default='')
    image = models.ImageField(default='', upload_to="../media")
    facilities = models.CharField(max_length=500, default='')
    # near_by_turf = models.CharField(max_length=500, default='')
    emergency = models.CharField(max_length=500, default='')
    events = models.CharField(max_length=500, default='')
    num_5v5 = models.IntegerField(default=0)
    price_per_hour_5v5 = models.IntegerField(default=500)
    num_7v7 = models.IntegerField(default=0)
    price_per_hour_7v7 = models.IntegerField(default=700)
    num_7v7_5v5 = models.IntegerField(default=0)
    num_12v12 = models.IntegerField(default=0)
    price_per_hour_12v12 = models.IntegerField(default=1200)

    def __str__(self):
        return self.name

# Reservation Model


# # creating a form
# class DetailsForm(forms.Form):

#     first_name = forms.CharField(max_length = 50)
#     last_name = forms.CharField(max_length = 50)
#     phone_number = forms.IntegerField
#     ground_name = forms.CharField(max_length = 50)
#     ground_address = forms.CharField(max_length = 200)



class Contact(models.Model):
    name = models.CharField(max_length=200, default='')
    emailid = models.EmailField(max_length=254, default='')
    message = models.CharField(max_length=2000, default='')
    

    def __str__(self):
        return self.name
