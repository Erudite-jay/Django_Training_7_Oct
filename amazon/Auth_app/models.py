from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254,primary_key=True)
    phone_number = models.CharField(max_length=10)
