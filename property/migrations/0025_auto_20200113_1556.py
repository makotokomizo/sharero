# Generated by Django 2.2 on 2020-01-13 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0024_auto_20200108_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
