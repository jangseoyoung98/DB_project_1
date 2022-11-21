import django_filters

from .models import Listing

class ListingFilter(django_filters.FilterSet):

    class Meta:
        model = Listing
        fields = { # https://gaussian37.github.io/python-django-django-query-set/
            '속성1':['exact'],
            '속성2':['icontains'],
            '속성3':['lt']
        }

