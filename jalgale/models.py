from django.core.checks import messages
from django.db import models
from django.db.models.base import Model
from ckeditor.fields import RichTextField
from django import forms

# Create your models here.

class Menu (models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class content_descriptions(models.Model):
    content_name = models.CharField(max_length = 100)
    content_desc = models.TextField()

class Project (models.Model):    
    name = models.CharField(max_length=100)
    desc= models.TextField(blank=True)
    img = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name

class ContactUs (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length= 200)
    message = models.TextField()
    def __str__(self):
        return self.name

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
    know_more = RichTextField(blank=True, null=True)

class Page (models.Model):
    slug = models.CharField(max_length=100)
    title = models.CharField(max_length= 200)
    sub_description = models.TextField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    def __str__(self):
        return self.title

class Testimonial (models.Model):    
    name = models.CharField(max_length=100)
    comment= models.TextField()
    img = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name

class Album (models.Model):    
    title = models.CharField(max_length=100)
    short_desc= models.TextField()
    img = models.ImageField(upload_to='images')
    def __str__(self):
        return self.title

class Gallery (models.Model):    
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images')
    album = models.ForeignKey(Album, on_delete=models.CASCADE,null=False,default='')
    def __str__(self):
        return self.title + ' - ' + self.album.title