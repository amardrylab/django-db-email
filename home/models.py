from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()

