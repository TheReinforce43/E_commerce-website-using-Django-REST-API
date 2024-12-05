from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveDestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from User.Serializer.group_serializer import (
    CreateGroupSerializer,
    GetGroupSerializer,
    PermissionSerializer
    
)

from django.contrib.auth.models import (
    Group,
    Permission
)


# create API for creating Permission 
class CreateListPermissionAPI(ListCreateAPIView):
    serializer_class=PermissionSerializer
    queryset=Permission.objects.all()


# Update,get by id and delete the  permissions 
class UpdateRetrieveDestroyPermissionAPI(RetrieveUpdateDestroyAPIView):
    serializer_class=PermissionSerializer
    queryset=Permission.objects.all()


# create API for creating a group 


class CreateGroupAPI(CreateAPIView):
    serializer_class=CreateGroupSerializer
    queryset=Group.objects.all()


class ListGroupsAPI(ListAPIView):
    serializer_class=GetGroupSerializer
    queryset=Group.objects.all()



class UpdateGroupAPI(UpdateAPIView):
    serializer_class=CreateGroupSerializer
    queryset=Group.objects.all()


class RetrieveDestroyGroupAPI(RetrieveDestroyAPIView):
    serializer_class=GetGroupSerializer
    queryset=Group.objects.all()






