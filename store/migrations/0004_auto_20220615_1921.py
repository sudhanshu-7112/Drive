# Generated by Django 2.2 on 2022-06-15 13:51

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_documents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='file',
            field=models.ImageField(upload_to=store.models.path),
        ),
    ]