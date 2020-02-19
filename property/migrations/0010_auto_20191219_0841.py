# Generated by Django 3.0 on 2019-12-18 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_property_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='area',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='property',
            name='beds_number',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='garages_number',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
