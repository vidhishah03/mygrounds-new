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
    ("5", "5"),
)


class Turf_List(models.Model):
    turf_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Turf Name', max_length=200, default='')
    address = models.CharField('Turf Address', max_length=500, default='')
    image = models.ImageField('Turf Image', default='', upload_to="../media")
    has_refreshments = models.BooleanField(default=False)
    has_first_aid = models.BooleanField(default=False)
    has_parking = models.BooleanField(default=False)
    events = models.CharField('Upcoming Events', max_length=500, default='')
    num_5v5_turfs = models.CharField(
        'Number Of Turfs [5v5 Size]', max_length=1, choices=max_sizes, default="0")
    price_per_hour_5v5_weekdays = models.IntegerField(
        'Price per Hour [WEEKDAYS]', default=500)
    weekdays_turf_opening_time = models.TimeField(
        auto_now=False, auto_now_add=False, default="00:00")
    weekdays_turf_closing_time = models.TimeField(
        auto_now=False, auto_now_add=False, default="00:00")
    price_per_hour_5v5_weekends = models.IntegerField(
        'Price per Hour [WEEKENDS]', default=700)
    weekends_turf_opening_time = models.TimeField(
        auto_now=False, auto_now_add=False, default="00:00")
    weekends_turf_closing_time = models.TimeField(
        auto_now=False, auto_now_add=False, default="00:00")

    def __str__(self):
        return self.name


# Reservation Model
class Booking(models.Model):
    username = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    booked_turf_name = models.ForeignKey(Turf_List, on_delete=models.CASCADE)
    num_5v5 = models.CharField(
        'Number Of Turfs', max_length=1, choices=max_sizes, default="0")
    hours = models.CharField(
        'Number Of Hours', max_length=1, choices=max_sizes, default="1")
    date = models.DateField(default=datetime.now)
    startTime = models.TimeField('Start Time', auto_now=False)


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
