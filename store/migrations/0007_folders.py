# Generated by Django 2.2 on 2022-06-17 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20220617_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='folders',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]