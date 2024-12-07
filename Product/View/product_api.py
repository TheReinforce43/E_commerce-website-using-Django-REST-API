from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveDestroyAPIView
)

# import related serializer and model 
from Product.Model.product_model import  ProductModel 
from Product.Serializer.product_serializer import (
    CreateProductSerializer,
    GetProductSerializer 
)

from rest_framework.permissions import IsAuthenticated


class CreateProductAPIView(CreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = CreateProductSerializer
    permission_classes=[IsAuthenticated]


class GetProductAPIView(ListAPIView):
    
    serializer_class = GetProductSerializer
    permission_classes=[IsAuthenticated]


    def get_queryset(self):
        queryset = ProductModel.objects.select_related('category','brand')

        category_id = self.request.query_params.get('category_id', None)
        brand_id = self.request.query_params.get('brand_id', None)

        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)

        if brand_id is not None:
            queryset = queryset.filter(brand_id=brand_id)

        queryset= queryset.order_by('-created_at')

        return queryset


class UpdateProductAPIView(UpdateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = CreateProductSerializer
    permission_classes=[IsAuthenticated]



class RetrieveDestroyProductAPIView(RetrieveDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = GetProductSerializer
    permission_classes=[IsAuthenticated]
