from django.contrib import messages
from django.shortcuts import render, redirect

from menu.filters import ListingFilter
from menu.models import Listing
from menu.forms import ListingForm # 추가할 것

def main_view(request):
    return render(request, 'main.html', {"name": "DB_project"})
    # 위에 거 수정

def home_view(request):
    listings = Listing.objects.all()
    listing_filter = ListingFilter(request.GET, queryset=listings)
    context = {
        'listing_filter' : listing_filter,
    }
    return render(request, "home.html", context)
    # context 사전형 객체를 세전째 선택적(optional) 인수로 받습니다. 인수로 지정된 context로 표현된 템플릿의 HttpResponse 객체가 반환됩니다.

def list_view(request):
    if request.method == 'GET':
        listing_form = ListingForm()
        return render(request, 'list.html', {'listing_form' : listing_form})

def listing_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        return render(request, 'listing.html', {'listing': listing, })
    except Exception as e:
        messages.error(request, f'Invalid UID {id} was provided for listing.')
        return redirect('home')
