
# include related view files 
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView

)
from rest_framework.views import APIView 
from rest_framework.response import Response    
from rest_framework import status 
from rest_framework.permissions import IsAuthenticated

# import related models 
from User.models import User

# import related serializer 

from User.Serializer.user_serializer import (
    SignUpSerializer,
    LoginSerializer,
    LogoutSerializer,
    GetUserSerializer
)


# create the signup api view 


class UserSignUpView(CreateAPIView):
    serializer_class = SignUpSerializer
    queryset = User.objects.all()


# create the login api view 
# since we using custom serializers , so we need to use api view 


class UserLoginView(APIView):

    def post(self,request,*args,**kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
    

# create the logout api view

class UserLogoutView(APIView):

    permission_classes=[IsAuthenticated]
    def post(self, request, *args, **kwargs):
        serializer = LogoutSerializer(data= request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Successfully logged out.'}, status=status.HTTP_200_OK)
    


# get user list 
class GetuserList_api(ListAPIView):
    queryset = User.objects.all()
    serializer_class = GetUserSerializer