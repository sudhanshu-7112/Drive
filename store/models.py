from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class documents(models.Model):
    file=models.ImageField(upload_to='images')