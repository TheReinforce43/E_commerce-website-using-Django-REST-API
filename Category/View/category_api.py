from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from Category.Model.category_model import CategoryModel 
from Category.Serializer.category_serializer import CategorySerializer
from rest_framework.permissions import IsAuthenticated



class CreateListCategoryView(ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAuthenticated]


class UpdateRetrieveDestroyCategoryView(RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

