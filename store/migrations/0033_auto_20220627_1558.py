# Generated by Django 2.2 on 2022-06-27 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0032_auto_20220623_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='recent',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 27, 15, 58, 54, 75421)),
        ),
    ]
