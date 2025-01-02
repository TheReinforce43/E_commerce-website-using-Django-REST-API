from django.db import models 


from Category.Model.category_model import CategoryModel 
from Brand.Model.brand_model import BrandModel



class ProductModel(models.Model):
    category= models.ForeignKey(CategoryModel,on_delete=models.CASCADE,related_name='category_products',null=True)
    brand = models.ForeignKey(BrandModel,on_delete=models.CASCADE,related_name='brand_products',null=True)
    name = models.CharField(max_length=100,unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    color=models.CharField(max_length=50,unique=True)

    # created_at=models.DateTimeField(auto_now_add=True)
    # updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
