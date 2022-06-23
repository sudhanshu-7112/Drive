from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class folders(models.Model):
    name=models.CharField(max_length=20)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    s=models.IntegerField(default=0)

class document(models.Model):
    file=models.FileField(upload_to='images')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    folder=models.ForeignKey(folders, on_delete=models.CASCADE)
    recent=models.DateTimeField(default=datetime.now())
    byte=models.BigIntegerField()
    type=models.CharField(max_length=7, default='file')
    delete=models.IntegerField(default=0)
    permanentdel=models.IntegerField(default=0)

class size(models.Model):
    type=models.CharField(max_length=15)
    size=models.IntegerField()

class ProfilePic(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    pic=models.ImageField(upload_to='profile')



