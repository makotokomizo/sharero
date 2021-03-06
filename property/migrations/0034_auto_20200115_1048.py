# Generated by Django 2.2 on 2020-01-15 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0033_auto_20200115_0858'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharableItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='共有物')),
            ],
        ),
        migrations.RemoveField(
            model_name='property',
            name='sharableItems',
        ),
        migrations.AddField(
            model_name='property',
            name='sharableItems',
            field=models.ManyToManyField(to='property.SharableItem', verbose_name='紐づく共有物'),
        ),
    ]
