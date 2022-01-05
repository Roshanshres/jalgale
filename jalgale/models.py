from django.core.checks import messages
from django.db import models
from django.db.models.base import Model
from ckeditor.fields import RichTextField
from django import forms

# Create your models here.

class Menu (models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255)

class content_descriptions(models.Model):
    content_name = models.CharField(max_length = 100)
    content_desc = models.TextField()

class Project (models.Model):    
    name = models.CharField(max_length=100)
    desc= models.TextField()
    img = models.ImageField(upload_to='images')

class ContactUs (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length= 200)
    message = models.TextField()

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

class Page (models.Model):
    slug = models.CharField(max_length=100)
    title = models.CharField(max_length= 200)
    sub_description = models.TextField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)


