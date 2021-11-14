from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=120)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=11)
    desc=models.TextField()
    date=models.DateField()
