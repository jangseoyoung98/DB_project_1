import uuid

from django.db import models

from menu.consts import CATEGORY, BRANDS


##########################################################
class Allergy(models.Model):
    allergy_id = models.IntegerField(primary_key=True)
    allergy_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'allergy'

    def __str__(self):
        return self.allergy_name


class Brand(models.Model):
    brand_id = models.IntegerField(primary_key=True)
    brand_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'brand'

    def __str__(self):
        return self.brand_name

class Menu(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    category = models.ForeignKey('MenuCategory', on_delete=models.CASCADE)
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

    def __str__(self):
        return self.menu_name

class MenuAllergy(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'menu_allergy'


class MenuCategory(models.Model):
    category_id = models.IntegerField(primary_key= True)
    category_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'menu_category'
##########################################################

"""
class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    category = models.ForeignKey('MenuCategory', choices=CATEGORY, on_delete=models.CASCADE)  # 해당 메뉴의 -> category.category_name 필요
    brand = models.ForeignKey('Brand', choices=BRANDS, on_delete=models.CASCADE)  # 해당 메뉴의 -> brand.brand_name 필요
    allergy = models.ForeignKey('MenuAllergy', on_delete=models.CASCADE)  # 해당 메뉴의 -> allergy.allergy_name 필요
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)  # 해당 메뉴의 -> menu_name, description, price (calorie, sugars, protein, satured_fat, sodium, caffeine) 필요

    # 이미지 -> 음료 사진 필요

    def __str__(self):
       return f'{self.id}\'s Listing - {self.menu.menu_name}'
"""




