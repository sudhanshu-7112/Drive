from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class document(models.Model):
    file=models.FileField(upload_to='images')

class loc(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    folder=models.CharField(max_length=15, default='new folder')
    file=models.ForeignKey(document, on_delete=models.CASCADE)

class folders(models.Model):
    name=models.CharField(max_length=20)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

