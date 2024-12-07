from django.urls import path 

from Product.View.product_api import (
    CreateProductAPIView,
    GetProductAPIView,
    UpdateProductAPIView,
    RetrieveDestroyProductAPIView
)


urlpatterns = [
    path('add/',CreateProductAPIView.as_view(),name='AddProduct'),
    path('list/',GetProductAPIView.as_view(),name='ListProduct'),
    path('update/<int:pk>',UpdateProductAPIView.as_view(),name='UpdateProduct'),
    path('retrieve/<int:pk>',RetrieveDestroyProductAPIView.as_view(),name='RetrieveProduct'),
    path('delete/<int:pk>',RetrieveDestroyProductAPIView.as_view(),name='DeleteProduct'),
]
