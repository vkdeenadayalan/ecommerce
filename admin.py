from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import  category,Product
from .models import  Product



admin.site.register(CustomUser,UserAdmin)
admin.site.register(category)
admin.site.register(Product)

