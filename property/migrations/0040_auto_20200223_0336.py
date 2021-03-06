# Generated by Django 2.2 on 2020-02-23 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0039_auto_20200131_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='property',
            name='includeAdditionalFee',
            field=models.NullBooleanField(choices=[(True, 'はい'), (False, 'いいえ')], verbose_name='公共料金は含まれていますか??'),
        ),
        migrations.AlterField(
            model_name='property',
            name='oneToOne',
            field=models.NullBooleanField(choices=[(True, 'はい'), (False, 'いいえ')], verbose_name='定員1名に独立した1部屋を提供できますか？？'),
        ),
        migrations.AlterField(
            model_name='property',
            name='ownerConfirm',
            field=models.NullBooleanField(choices=[(True, 'はい'), (False, 'いいえ')], verbose_name='物件所有者は登録者様ですか？？'),
        ),
        migrations.AlterField(
            model_name='property',
            name='petsPermission',
            field=models.NullBooleanField(choices=[(True, 'はい'), (False, 'いいえ')], verbose_name='ペットを許可しますか??'),
        ),
        migrations.AlterField(
            model_name='property',
            name='smokingPersiion',
            field=models.NullBooleanField(choices=[(True, 'はい'), (False, 'いいえ')], verbose_name='喫煙を許可しますか??'),
        ),
        migrations.AlterField(
            model_name='property',
            name='visiterPersiion',
            field=models.NullBooleanField(choices=[(True, 'はい'), (False, 'いいえ')], verbose_name='メイトの友達の招待を許可しますか??'),
        ),
        migrations.AlterField(
            model_name='property',
            name='visiterStayPersiion',
            field=models.NullBooleanField(choices=[(True, 'はい'), (False, 'いいえ')], verbose_name='メイトの友達の宿泊を許可しますか??'),
        ),
        migrations.AlterField(
            model_name='property',
            name='workingNow',
            field=models.NullBooleanField(choices=[(True, 'はい'), (False, 'いいえ')], verbose_name='現在もお仕事されていますか??'),
        ),
    ]
