# Generated by Django 3.0 on 2019-12-19 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20191219_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(null=True, upload_to='property/'),
        ),
    ]
