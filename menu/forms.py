import re # re 모듈 제공 함수 사용
from django import forms

from .models import Listing


class ListingForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Listing
        fields = {'brand', }
        ## 필드 채워넣기