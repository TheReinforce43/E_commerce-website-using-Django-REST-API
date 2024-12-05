from rest_framework import serializers 
from django.contrib.auth.models import Permission,Group



class PermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model=Permission 
        fields = ['id', 'name', 'codename', 'content_type']



class CreateGroupSerializer(serializers.ModelSerializer):

    # Permission= serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all(),many=True)


    class Meta:
        model = Group 
        fields = '__all__'



class GetGroupSerializer(serializers.ModelSerializer):
    Permission= PermissionSerializer(read_only=True,many=True)


    class Meta:
        model = Group
        fields = '__all__'

