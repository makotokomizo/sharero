# Generated by Django 2.2 on 2020-03-02 02:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0010_auto_20200301_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectaccount',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='connect_account', to=settings.AUTH_USER_MODEL),
        ),
    ]
