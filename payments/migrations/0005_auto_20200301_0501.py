# Generated by Django 2.2 on 2020-03-01 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payments', '0004_plan_plan_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='description',
            field=models.TextField(blank=True, verbose_name='説明'),
        ),
        migrations.CreateModel(
            name='connect_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connect_id', models.CharField(max_length=30, verbose_name='connect_id')),
                ('first_name_kanji', models.CharField(max_length=20, verbose_name='下の名前（漢字）')),
                ('first_name_kana', models.CharField(max_length=20, verbose_name='下の名前（かな）')),
                ('last_name_kanji', models.CharField(max_length=20, verbose_name='上の名前（漢字）')),
                ('last_name_kana', models.CharField(max_length=20, verbose_name='上の名前（かな）')),
                ('birth_date', models.DateTimeField()),
                ('gender', models.CharField(max_length=200, verbose_name='性別')),
                ('post_code', models.CharField(max_length=200, verbose_name='郵便番号')),
                ('address_kanji', models.CharField(max_length=200, verbose_name='住所（漢字）')),
                ('address_kana', models.CharField(max_length=200, verbose_name='住所（かな）')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address')),
                ('phone_number', models.CharField(max_length=11, verbose_name='電話番号')),
                ('object', models.CharField(default='bank_account', max_length=20, verbose_name='タイプ')),
                ('account_number', models.CharField(max_length=20, verbose_name='account_number')),
                ('bank_code', models.CharField(max_length=20, verbose_name='銀行コード')),
                ('branch_code', models.CharField(max_length=3, verbose_name='支店コード')),
                ('routing_number', models.CharField(max_length=20, verbose_name='account_number')),
                ('account_holder_name', models.CharField(max_length=20, verbose_name='名義人')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
