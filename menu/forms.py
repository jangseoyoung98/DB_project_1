from django import forms

from .models import Listing


class ListingForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Listing
        fields = {'brand.brand_name',
                  'menu.menu_name',
                  'menu.description',
                  'menu.size',
                  'menu.calorie', 'menu.sodium',
                  'menu.saturated_fat', 'menu.sugar',
                  'menu.protein', 'menu/caffeine'}