from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=100)


class Product(models.Model):

    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    

