import uuid

from django.db import models



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

    def __str__(self):
        return self.menu.menu_name


class MenuCategory(models.Model):
    category_id = models.IntegerField(primary_key= True)
    category_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'menu_category'

    def __str__(self):
        return self.category_name
##########################################################



