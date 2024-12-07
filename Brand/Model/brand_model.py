from django.db import models 



class BrandModel(models.Model):

    brand_name = models.CharField(max_length=50, unique=True)
    origin_country = models.CharField(max_length=250,null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.brand_name