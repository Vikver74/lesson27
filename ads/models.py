from django.db import models

# Create your models here.


class Ad(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=400, null=True)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=30)
