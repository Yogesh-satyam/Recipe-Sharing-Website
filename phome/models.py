from unicodedata import category
from django.db import models

# Create your models here.

class Cuisines_category(models.Model):
    name=models.CharField(default=None, null=True,max_length=50)
    desp=models.CharField(default=None, null=True,max_length=500)
    path=models.CharField(default=None, null=True,max_length=100)