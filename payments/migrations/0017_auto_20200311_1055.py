# Generated by Django 2.2 on 2020-03-11 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0016_auto_20200311_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectaccount',
            name='phone_number',
            field=models.CharField(max_length=11, null=True, unique=True, verbose_name='電話番号'),
        ),
    ]
