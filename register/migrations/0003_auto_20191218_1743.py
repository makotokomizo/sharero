# Generated by Django 3.0 on 2019-12-18 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_user_is_nester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='norp',
        ),
        migrations.AddField(
            model_name='user',
            name='price',
            field=models.CharField(blank=True, max_length=20, verbose_name='家賃'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='年齢'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('1', '女性'), ('2', '男性')], max_length=2, verbose_name='gender性別'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=150, verbose_name='last name'),
        ),
    ]
