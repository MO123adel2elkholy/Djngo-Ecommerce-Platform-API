from django.contrib import admin
from .models import Category ,Product , ProductInventory , ProductType , Brand , Media ,Stock
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductInventory)
admin.site.register(ProductType)
admin.site.register(Brand)
admin.site.register(Media)
admin.site.register(Stock)
