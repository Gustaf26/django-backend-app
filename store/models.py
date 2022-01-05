from django.db import models

# Create your models here.

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
