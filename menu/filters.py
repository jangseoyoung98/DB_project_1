import django_filters

from .models import Allergy, Brand, Menu, MenuAllergy, MenuCategory

class ProductFilter(django_filters.Filterset):

    class Meta:
        model = Allergy, Brand, Menu, MenuAllergy, MenuCategory
        fields = {
            'brand'
        }
        """
        - 브랜드, 카테고리, 알레르기 → 체크 박스
        - 칼로리, 가격, 카페인 → 스크롤 선택
        """