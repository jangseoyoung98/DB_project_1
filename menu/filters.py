import django_filters

from .models import Listing

class ProductFilter(django_filters.Filterset):

        class Meta:
            model = Listing
            fields = {
                'brand_name': ['exact'],
                'category_name': ['exact'],
                'allergy_name': ['icontains'],
                ###
                # 'calorie':
                # 'price' :
                # 'caffeine':

            }

        """
        - 브랜드, 카테고리, 알레르기 → 체크 박스
        - 칼로리, 가격, 카페인 → 스크롤 선택
        """