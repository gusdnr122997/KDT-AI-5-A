from django.db import models

# Create your models here.
class Coffee(models.Model):
    def __str__(self):
        return self.name

    cid = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=30, unique=True)
    price = models.IntegerField(default=0)
    is_ice = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)


class Burger(models.Model):

    def __str__(self):
        return self.name
    
    bid = models.AutoField(primary_key=True)
    name = models.CharField(default="", max_length=40, unique=True)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)