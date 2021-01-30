import django_filters

from .models import *

class Turf_ListFilter(django_filters.FilterSet):
    class Meta:
        model = Turf_List
        fields = '__all__'
        exclude = ['image','weekdays_turf_opening_time','weekdays_turf_closing_time','events','turf_id',
        'weekdends_turf_opening_time','weekends_turf_closing_time','price_per_hour_5v5_weekdays','price_per_hour_5v5_weekends']