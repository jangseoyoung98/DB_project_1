# Generated by Django 4.1.3 on 2022-11-26 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('allergy_id', models.IntegerField(primary_key=True, serialize=False)),
                ('allergy_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'allergy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_id', models.IntegerField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'brand',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('menu_id', models.IntegerField(primary_key=True, serialize=False)),
                ('menu_name', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=100)),
                ('calorie', models.FloatField(blank=True, null=True)),
                ('sugars', models.FloatField(blank=True, null=True)),
                ('protein', models.FloatField(blank=True, null=True)),
                ('saturated_fat', models.FloatField(blank=True, null=True)),
                ('sodium', models.FloatField(blank=True, null=True)),
                ('caffeine', models.FloatField(blank=True, null=True)),
                ('size', models.IntegerField()),
                ('description', models.CharField(db_collation='utf8mb4_0900_ai_ci', max_length=200)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MenuAllergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'menu_allergy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'menu_category',
                'managed': False,
            },
        ),
    ]
