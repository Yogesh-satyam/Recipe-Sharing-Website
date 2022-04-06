from unicodedata import category
from django.db import models

# Create your models here.

class Cuisines_category(models.Model):
    name:models.CharField(max_length=50)
    desp:models.CharField(max_length=500)