# Generated by Django 2.2 on 2022-06-18 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_auto_20220618_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='recent',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 18, 23, 17, 52, 201815)),
        ),
    ]