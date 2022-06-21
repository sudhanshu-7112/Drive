# Generated by Django 2.2 on 2022-06-20 18:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0025_auto_20220620_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='recent',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 21, 0, 13, 39, 538911)),
        ),
        migrations.CreateModel(
            name='ProfilePic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
