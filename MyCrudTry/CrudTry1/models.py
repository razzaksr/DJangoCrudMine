from django.db import models

# Create your models here.

class Laptop(models.Model):
    version=models.CharField(max_length=50)
    brand=models.CharField( max_length=50)
    price=models.FloatField()
    class Meta:
        db_table="laptop"