# Generated by Django 3.0 on 2019-12-20 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20191220_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(null=True, upload_to='property/'),
        ),
    ]
