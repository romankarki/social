from .models import User 
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    # serializer for the modifield user
    class Meta:
    	model = User
    	fields= "__all__"

    