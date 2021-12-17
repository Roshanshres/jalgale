from django.db import models
from django.db.models.base import Model

# Create your models here.

class Menu (models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255)

class Project (models.Model):
    name = models.CharField(max_length=100)
    desc= models.TextField()
    img = models.ImageField(upload_to='images')

class Sitesetting (models.Model):
    logo = models.ImageField(upload_to='images')
    facebook_url = models.CharField(max_length=100)
    twitter_url = models.CharField(max_length=100)
    instagram_url = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    company_brief = models.CharField(max_length=100)
    google_map= models.TextField()


