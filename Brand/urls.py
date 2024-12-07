from django.urls import path 

from Brand.View.brand_api import (
    CreateListBrandView,
    UpdateRetrieveDestroyBrandView
)


urlpatterns = [
    
    path('add/',CreateListBrandView.as_view(),name='create'),
    path('list/',CreateListBrandView.as_view(),name='list'),
    path('update/<int:pk>',UpdateRetrieveDestroyBrandView.as_view(),name='update'),
    path('retrieve/<int:pk>',UpdateRetrieveDestroyBrandView.as_view(),name='retrieve'),
    path('delete/<int:pk>',UpdateRetrieveDestroyBrandView.as_view(),name='delete'),
]
