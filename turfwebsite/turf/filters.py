import django_filters

from .models import *

class Turf_ListFilter(django_filters.FilterSet):
    class Meta:
        model = Turf_List
        fields = '__all__'
        exclude = ['image','has_refreshments','events','turf_id']