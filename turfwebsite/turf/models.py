import uuid
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime

max_sizes = (
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
)


class Turf_List(models.Model):
    turf_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=500, default='')
    image = models.ImageField(default='', upload_to="../media")
    has_refreshments = models.BooleanField(default=False)
    has_first_aid = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)
    events = models.CharField(max_length=500, default='')
    num_5v5_turfs = models.CharField(
        max_length=1, choices=max_sizes, default="0")
    price_per_hour_5v5 = models.IntegerField(default=500)

    def __str__(self):
        return self.name


# Reservation Model
class Booking(models.Model):
    startTime = models.DateTimeField(default=datetime.now, blank=True)
    endTime = models.DateTimeField(default=datetime.now, blank=True)
    num_5v5 = models.CharField(max_length=1, choices=max_sizes, default="0")
    booked_turf_id = models.ForeignKey(
        Turf_List, on_delete=models.CASCADE, default='')
    guest = models.ForeignKey(User, default='', on_delete=models.CASCADE)


class Contact(models.Model):
    name = models.CharField(max_length=200, default='')
    emailid = models.EmailField(max_length=254, default='')
    message = models.CharField(max_length=2000, default='')

    def __str__(self):
        return self.name


class feedback(models.Model):
    image = models.ImageField(default='', upload_to="../media")
    message = models.TextField(default='')

    def __str__(self):
        return self.message
