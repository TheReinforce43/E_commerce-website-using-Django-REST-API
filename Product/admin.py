from django.contrib import admin

# Register your models here.

from Product.Model.product_model import ProductModel 

admin.site.register(ProductModel)
