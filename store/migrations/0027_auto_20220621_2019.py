# Generated by Django 2.2 on 2022-06-21 14:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_auto_20220621_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='recent',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 20, 19, 53, 786162)),
        ),
        migrations.AlterField(
            model_name='folders',
            name='s',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
