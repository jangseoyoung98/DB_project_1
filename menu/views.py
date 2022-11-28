from django.shortcuts import render

from menu.models import *
from .category import CategoryForm
from .filters import MenuFilter

def home_view(request):
    if request.method == 'GET':
        brands = CategoryForm.Brand.names_b
        categorys = CategoryForm.MenuCategory.names_c
        # allergys = CategoryForm.Allergy.names_a

        return render(request, "home.html", {"brands": brands, "categorys": categorys})

    if request.method == 'POST':
        listings = Menu.objects.all()
        listing_filter = MenuFilter(request.GET, queryset=listings)
        brands = CategoryForm.Brand.names_b
        categorys = CategoryForm.MenuCategory.names_c
        # allergys = CategoryForm.Allergy.names_a

        searched = request.POST
        calorie = searched["calorie"]
        price = searched["money"]
        caffeine = searched["caffeine"]
        brand_id = searched["brands"]
        category_id = searched["categorys"]
        # allergy_id = searched["allergys"]

        queryset_1 = Menu.objects.filter(brand_id=brand_id, category_id=category_id, price__lt=price, calorie__lt=calorie, caffeine__lt=caffeine)
        print(queryset_1)

        context = {
            "brands": brands,
            "categorys": categorys,
            # "allergys": allergys,

            'listing_filter': listing_filter,
            "listings": queryset_1
        }

        return render(request, 'home.html', context)
