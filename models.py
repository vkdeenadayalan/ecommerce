from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
import datetime
import os


def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('static/images',new_filename)



class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=20)
    
    
class category(models.Model):
    name=models.CharField(null=False, blank=True,max_length=255)
    cat_slug=models.SlugField(unique=True,max_length=250)
    description=models.TextField(max_length=30)
    sort_order=models.IntegerField(null=False, blank=True)
    image=models.ImageField(upload_to=getFileName, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(null=False, blank=True)
    
    def save(self, *args, **kwargs):
        self.pro_slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name

class Product(models.Model):   
    categories=models.ForeignKey(category, on_delete=models.CASCADE)
    name=models.CharField(null=False, blank=True,max_length=255)
    pro_slug=models.SlugField(unique=True,max_length=250)
    price=models.IntegerField(null=False,blank=True)
    sort_order=models.IntegerField(null=False, blank=True)
    image=models.ImageField(upload_to=getFileName, null=True, blank=True)
    description=models.TextField(null=False, blank=True)
    quantity=models.IntegerField(null=False, blank=True)
    
    def save(self, *args, **kwargs):
        self.pro_slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
        
        
   