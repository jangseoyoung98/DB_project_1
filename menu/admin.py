from django.contrib import admin
from .models import Allergy, Brand, Menu, MenuAllergy, MenuCategory

admin.site.register(Allergy)
admin.site.register(Brand)
admin.site.register(Menu)
admin.site.register(MenuAllergy)
admin.site.register(MenuCategory)

