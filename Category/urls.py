from django.urls import path 


from Category.View.category_api import (
    CreateListCategoryView,
    UpdateRetrieveDestroyCategoryView
)


urlpatterns = [
    path('add/',CreateListCategoryView.as_view(),name='add'),
    path('list/',CreateListCategoryView.as_view(),name='list'),
    path('update/<int:pk>',UpdateRetrieveDestroyCategoryView.as_view(),name='update'),
    path('retrieve/<int:pk>',UpdateRetrieveDestroyCategoryView.as_view(),name='retrieve'),
    path('delete/<int:pk>',UpdateRetrieveDestroyCategoryView.as_view(),name='delete'),
]
