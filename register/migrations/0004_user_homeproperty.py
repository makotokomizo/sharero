# Generated by Django 3.0 on 2019-12-20 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20191219_1038'),
        ('register', '0003_auto_20191218_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='homeProperty',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='homeProperty', to='property.Property'),
        ),
    ]
