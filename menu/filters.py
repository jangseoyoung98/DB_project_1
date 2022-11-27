import django_filters

from .models import Allergy, Brand, Menu, MenuAllergy, MenuCategory

"""
class ProductFilter(django_filters.Filterset):

        class Meta:
            model = Listing
            fields = {
                'brand.brand_name': ['exact'],
                'category.category_name': ['exact'],
                'allergy.allergy_name': ['icontains'], # 다중 필터로 변경
                'menu.calorie': ['lt'] # 다른 걸로 한 번 시도해보기
                # 'price' :
                # 'caffeine':
            }

class ProductFilter(django_filters.Filterset):

        def check_brand(self):
        class Meta:
            model = Allergy
            fields = {
                    'allergy_name': ['icontains']
            }

        class Meta:
                model = Brand
                fields = {
                        'brand_name': ['exact']
                }
"""

"""
- 브랜드, 카테고리, 알레르기 → 체크 박스
- 칼로리, 가격, 카페인 → 스크롤 선택
"""