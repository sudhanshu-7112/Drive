# Generated by Django 2.2 on 2022-06-23 12:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_auto_20220623_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='recent',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 23, 18, 5, 16, 749498)),
        ),
        migrations.AlterField(
            model_name='folders',
            name='s',
            field=models.IntegerField(default=0),
        ),
    ]
