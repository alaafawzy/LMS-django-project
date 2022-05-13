from distutils.command.upload import upload
from statistics import mode
from telnetlib import STATUS
from turtle import title
from unicodedata import category, name
from django.db import models

# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) :
        return self.name

class Books(models.Model):

    status_books = [
        ('available','available'),
        ('rental','rental'),
        ('sold','sold'),
    ]

    title = models.CharField(max_length=250)
    auther = models.CharField(max_length=250,null=True,blank=True)
    book_pic = models.ImageField(upload_to = 'photos',null=True,blank=True)
    auther_pic = models.ImageField(upload_to = 'photos',null=True,blank=True)
    pages = models.IntegerField(null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    rental_price= models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    rental_period = models.IntegerField(null=True,blank=True)
    total_rentalprice= models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField( max_length=50, choices=status_books,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,null=True,blank=True)
    
    def __str__(self) :
        return self.title

