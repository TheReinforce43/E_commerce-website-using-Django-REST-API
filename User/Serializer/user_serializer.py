from rest_framework import serializers 
# from User.models import User 

# add related modules for authentication
from rest_framework_simplejwt.tokens import RefreshToken 
from django.contrib.auth import authenticate 
from django.contrib.auth.models import  Group
from django.contrib.auth import get_user_model

User = get_user_model()

# sign up serializer of a user  

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    groups= serializers.PrimaryKeyRelatedField(queryset= Group.objects.all(),many=True)

    class Meta:
        model = User

        fields =  ['name', 'email', 'phone_number','is_staff', 'password', 'profile_image','groups']
        # extra_kwargs = {'password': {'write_only': True}}


    def create(self,validated_data):
        password= validated_data.pop('password')
        groups = validated_data.pop('groups', [])
        user= User.objects.create_user(**validated_data)
        user.set_password(password)   #has the password
        user.save()


        # Add user to groups if any
        user.groups.set(groups)
        
        return user
         


# logged in serializer 
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        # Authenticate the user
        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid email or password")
        if not user.is_active:
            raise serializers.ValidationError("This account is inactive")

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)

        return {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        }

# logout serializer 


class LogoutSerializer(serializers.Serializer):
    refresh_token =serializers.CharField()

    def validate(self,data):
        self.RefreshToken= data['refresh_token']
        return data 
    
    def save(self,**kwargs):

        try:
            token = RefreshToken(self.refresh_token)
            token.blacklist()
        
        except Exception as e:
            raise serializers.ValidationError("Invalid token or expire")



# Get User serializer 

class GetUserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User 
        fields='__all__'