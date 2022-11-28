from django import forms

from .models import *


class CategoryForm(forms.ModelForm):
    # image = forms.ImageField()

    class Brand:
        brands = Brand.objects.all()
        names_b = []
        for i in brands:
            names_b.append({"brand_name": i.brand_name, "id": i.brand_id})

    class MenuCategory:
        categorys = MenuCategory.objects.all()
        names_c = []
        for i in categorys:
            names_c.append({"category_name": i.category_name, "id": i.category_id})


