import django_filters

from .models import Listing

class ListingFilter(django_filters.Filterset):

    class Meta:
        model = Listing
        fields = {'brand' : ['exact'], 'category' : ['exact'], 'allergy' : ['icontains'],
                  'menu':[]}
        """
        - 브랜드, 카테고리, 알레르기 → 체크 박스
        - 칼로리, 가격, 카페인 → 스크롤 선택
        """