from imp import reload

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.shortcuts import render

from menu.filters import ProductFilter
from menu.forms import ListingForm
from menu.models import Listing

def main_view(request):
    listings = Listing.objects.all()
    listing_filter = ProductFilter(request.GET, queryset=listings)
    context = {
        'listing_filter': listing_filter
    }
    return render(request, 'templates/main.html', context)

def list_view(request):
    if request.method == 'POST':
        try:
            listing_form = ListingForm(request.POST, request.FILES)
            if listing_form.is_valid():
                listing = listing_form.save(commit=False)
                listing.save()
                messages.info(
                    request, f'{listing.model} Listing Posted Successfully!')
                return redirect('main')
            else:
                raise Exception()
        except Exception as e:
            print(e)
            messages.error(
                request, 'An error occured while posting the listing.')
    elif request.method == 'GET':
        listing_form = ListingForm()
        return render(request, 'templates/product.html', {'listing_form': listing_form})

def listing_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        return render(request, 'views/listing.html', {'listing': listing, })
    except Exception as e:
        messages.error(request, f'Invalid UID {id} was provided for listing.')
        return redirect('home')


