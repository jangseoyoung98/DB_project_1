import uuid
from django.db import models


##########################################################
class Allergy(models.Model):
    allergy_id = models.IntegerField(primary_key=True)
    allergy_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'allergy'


class Brand(models.Model):
    brand_id = models.IntegerField(primary_key=True)
    brand_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'brand'


class Menu(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    brand = models.ForeignKey(Brand, models.DO_NOTHING)
    category = models.ForeignKey('MenuCategory', models.DO_NOTHING)
    menu_name = models.CharField(max_length=100, db_collation='utf8mb4_0900_ai_ci')
    calorie = models.FloatField(blank=True, null=True)
    sugars = models.FloatField(blank=True, null=True)
    protein = models.FloatField(blank=True, null=True)
    saturated_fat = models.FloatField(blank=True, null=True)
    sodium = models.FloatField(blank=True, null=True)
    caffeine = models.FloatField(blank=True, null=True)
    size = models.IntegerField()
    description = models.CharField(max_length=200, db_collation='utf8mb4_0900_ai_ci')
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'menu'


class MenuAllergy(models.Model):
    menu = models.ForeignKey(Menu, models.DO_NOTHING)
    allergy = models.ForeignKey(Allergy, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'menu_allergy'


class MenuCategory(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'menu_category'
##########################################################

class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    category = models.ForeignKey('MenuCategory', models.DO_NOTHING)
    brand = models.ForeignKey(Brand, models.DO_NOTHING) # 브랜드명 필요
    allergy = models.ForeignKey(MenuAllergy, models.DO_NOTHING)
    image = models.ImageField()
    # 이미지 -> 음료 사진 필요
    menu = models.ForeignKey(Menu, models.DO_NOTHING) 
    # 메뉴명, 메뉴 설명, 영양성분 필요

    """
    def __str__(self):
        return f'{self.seller.user.username}\'s Listing - {self.model}'
    """






