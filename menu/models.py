import uuid
from django.db import models

from .consts import CAFE_BRANDS, TRANSMISSION_OPTIONS


class Listing(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    # 속성 채워넣기
    

    def __str__(self):
        return f'{self.seller.user.username}\'s Listing - {self.model}'
