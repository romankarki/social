from .models import User 
from rest_framework import serializers
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    # serializer for the modifield user
    class Meta:
    	model = User
    	fields= ["id","username","full_name","profile_picture","address","email"]


class UserRegisterSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ["id","username","email","password"]
		extra_kwargs = {"password":{"write_only":True}}

	def create(self,validated_data):
		user = User.objects.create_user(
			validated_data['username'],validated_data['email'],validated_data["password"],
			)
		return user


class UserShowSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ["id","username","full_name"]

class LoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()

	def validate(self,data):
		user = authenticate(**data)
		if user and user.is_active:
			return user
		raise serializers.ValidationError("Please provide the correct Credentials!!")



    