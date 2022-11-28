from django.shortcuts import redirect, render, get_object_or_404

from menu.models import *
from .category import CategoryForm
from .filters import MenuFilter

def home_view(request):
    if request.method == 'GET':
        brands = CategoryForm.Brand.names_b
        categorys = CategoryForm.MenuCategory.names_c
        # allergys = CategoryForm.Allergy.names_a

        return render(request, "home.html", {"brands": brands, "categorys": categorys, "allergys": allergys})

    if request.method == 'POST':
        listings = Menu.objects.all()
        listing_filter = MenuFilter(request.GET, queryset=listings)
        brands = CategoryForm.Brand.names_b
        categorys = CategoryForm.MenuCategory.names_c
        # allergys = CategoryForm.Allergy.names_a

        searched = request.POST
#        calorie = searched["calorie"]
        price = searched["money"]
#        caffeine = searched["caffeine"]
        brand_id = searched["brands"]
        category_id = searched["categorys"]
        # allergy_id = searched["allergys"]

        # allergy 수정 - 이 id에 포함된 메뉴_id를 파악해서 그 음료들은 exclude
        queryset_1 = Menu.objects.filter(brand_id=brand_id, category_id=category_id, price__lt=price)
        print(queryset_1)

        context = {
            "brands": brands,
            "categorys": categorys,
            # "allergys": allergys,

            'listing_filter': listing_filter,
            "listings": queryset_1
        }

        return render(request, 'home.html', context)

"""
def home_view(request):
    listings = Listing.objects.all()
    listing_filter = ProductFilter(request.GET, queryset=listings)
    context = {
        'listing_filter': listing_filter
    }
    return render(request, 'templates/home.html', context)

def list_view(request):
    if request.method == 'GET':
        listing_form = ListingForm()
        return render(request, 'templates/list.html', {'listing_form': listing_form})

def listing_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        return render(request, 'views/listing.html', {'listing': listing, })
    except Exception as e:
        messages.error(request, f'Invalid UID {id} was provided for listing.')
        return redirect('home')


"""