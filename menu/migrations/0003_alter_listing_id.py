# Generated by Django 4.1.3 on 2022-11-26 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_listing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
