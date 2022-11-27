from imp import reload

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404

from menu.filters import ProductFilter
from menu.forms import ListingForm
from menu.models import Listing

def main_view(request):
    return render(request, "templates/main.html", {"name": "cafe_db"})

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


