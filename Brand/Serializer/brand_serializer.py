from rest_framework import serializers 
from Brand.Model.brand_model import BrandModel 



class BrandSerializer(serializers.ModelSerializer):


    class Meta:
        model=BrandModel
        fields='__all__'

    def validate(self, attrs):
        # Extract brand_name from attributes
        brand_name=attrs.get('brand_name')

        if self.instance :
            
            # this case checks during updating api 
            if BrandModel.objects.filter(brand_name=brand_name).exclude(pk=self.instance.pk).exists():
                raise serializers.ValidationError('Brand Name already exists')
            
            # this case checks during creating new brand

        else:
            if BrandModel.objects.filter(brand_name=brand_name).exists():
                raise serializers.ValidationError('Brand Name already exists')
            
        return attrs 
                
        
            



        