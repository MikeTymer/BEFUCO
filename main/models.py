from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class CompanyDetails(models.Model):
    sitename = models.CharField(max_length=25)
    logo = models.ImageField(upload_to='images/Companylogo')
    nav_button_name = models.CharField(max_length=25)
    nav_button_link = models.URLField()
    welcome_message = models.TextField()
    contact = models.IntegerField()
    whatsapp = models.URLField()
    facebook = models.URLField()
    email = models.EmailField()
    address = models.CharField(max_length = 50)
    who_we_are = models.TextField()
    how_we_help = models.TextField()
    about_us = models.TextField()
    disclaimer = models.TextField()
    full_disclaimer = models.TextField()
    address_image = models.ImageField(upload_to='images/addressImage')
    copyright = models.CharField(max_length=50)
    shopping_link = models.URLField()
    embedded_video_source = models.URLField()
  

    def __str__(self):
        return self.sitename

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    mini_description= models.TextField()
    description = models.TextField()
    views = models.PositiveIntegerField(default=0)
    post_date = models.DateField(default=date.today)
    slug = models.CharField(max_length=100, null=True, blank=True)
    featured_image = models.ImageField(upload_to='images/category/')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["post_date"]
    

    
class Blog(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    description = models.TextField()
    mini_description = models.TextField()
    post_date = models.DateField(default=date.today)
    slug = models.CharField(max_length=100, null=True, blank=True)
    feature_image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " ==> " + str(self.author)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + str(self.post_date))
        return super().save(*args, **kwargs)
    
    class Meta:
        ordering = ["post_date"]

   
class BlogComment(models.Model):
    description = models.TextField(help_text="Write your comment")
    name = models.CharField(max_length=30, help_text ="Write your full name here")
    #author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.blog)
    
    class Meta:
        ordering = ["comment_date"]

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    e_mail = models.EmailField(max_length=250)
    contact_date = models.DateTimeField(default=date.today)
    phone_number = models.IntegerField()
    contact_message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return str(self.first_name + " " + self.last_name)

    class Meta:
        ordering = ["contact_date"]

    
    