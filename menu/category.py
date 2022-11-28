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

    class Allergy:
        allergys = Allergy.objects.all()
        allergy_menu = MenuAllergy.objects.all()
        names_a = []
#        menus_a = []
        for i in allergys:
            names_a.append({"allergy_name": i.allergy_name, "id": i.allergy_id})

