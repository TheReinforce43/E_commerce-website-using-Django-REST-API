from rest_framework import serializers 
from Product.Model.product_model import ProductModel


# import related serializers 

from Category.Serializer.category_serializer import CategorySerializer 
from Brand.Serializer.brand_serializer import BrandSerializer  


class CreateProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductModel
        fields = '__all__'


class GetProductSerializer(serializers.ModelSerializer):

    category=CategorySerializer(read_only=True,many=False)
    brand= BrandSerializer(read_only=True,many=False)


    class Meta:
        model = ProductModel
        fields = '__all__'





