
from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    detail = HTMLField()

    new_slug = AutoSlugField(populate_from='name',unique=True,null=True,default=None)# Slug


class Team(models.Model):
    t_name = models.CharField(max_length=100)
    t_origin = models.IntegerField()
    t_desc = HTMLField()
    t_file = models.FileField(upload_to='team/',max_length=250,null=True,default=None) # uploading image
# Create your models here.
