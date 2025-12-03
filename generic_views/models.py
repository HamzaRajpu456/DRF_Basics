from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(null=True)


class Product(models.Model):

    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    

