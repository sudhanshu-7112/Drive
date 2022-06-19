from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class folders(models.Model):
    name=models.CharField(max_length=20)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    size=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class document(models.Model):
    file=models.FileField(upload_to='images')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    folder=models.ForeignKey(folders, on_delete=models.CASCADE)
    recent=models.DateTimeField(default=datetime.now())
    byte=models.BigIntegerField()

class size(models.Model):
    type=models.CharField(max_length=15)
    size=models.IntegerField()



