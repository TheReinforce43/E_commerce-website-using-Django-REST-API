from rest_framework.generics import  (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

# import all related serializers 

from  Brand.Serializer.brand_serializer import BrandSerializer

# import all related models

from Brand.Model.brand_model import BrandModel

# import permission classes

from rest_framework.permissions import IsAuthenticated



class CreateListBrandView(ListCreateAPIView):
    queryset = BrandModel.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]



class UpdateRetrieveDestroyBrandView(RetrieveUpdateDestroyAPIView):
    queryset = BrandModel.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticated]


