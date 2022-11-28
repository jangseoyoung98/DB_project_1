from django.conf import settings
from django.urls import path

# from .views import main_view, home_view, list_view, listing_view
from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    # path('home/', home_view, name='home'),
    # path('list/', list_view, name='list'),
    # path('listing/<str:id>/', listing_view, name='listing'),
]