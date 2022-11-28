import django_filters

from .models import Menu


class MenuFilter(django_filters.FilterSet):

    class Meta:
        model = Menu
        fields = {'price': ['lt'],
                  'calorie': ['lt'],
                  'caffeine': ['lt']}
