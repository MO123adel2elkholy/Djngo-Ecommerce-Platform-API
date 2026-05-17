from django.contrib import admin
from .models import Category ,Product , ProductInventory , ProductType , Brand , Media ,Stock, ProductAttribute ,ProductAttributeValue , ProductAttributeValues ,ProductTypeAttribute
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductInventory)
admin.site.register(ProductType)
admin.site.register(Brand)
admin.site.register(Media)
admin.site.register(Stock)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
admin.site.register(ProductAttributeValues)
admin.site.register(ProductTypeAttribute)
