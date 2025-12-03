from django.db import models

class Market(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='markets/')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

    def __str__(self):
        return self.name