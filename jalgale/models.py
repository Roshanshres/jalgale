from django.db import models
from django.db.models.base import Model

# Create your models here.


class Project (models.Model):
   
    name = models.CharField(max_length=100)
    desc= models.TextField()
    img = models.ImageField(upload_to='images')


