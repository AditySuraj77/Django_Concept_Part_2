from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    desc = models.TextField()

# Create your models here.
