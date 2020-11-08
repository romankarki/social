from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import UserRegisterSerializer, LoginSerializer, UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken

# Create your views here.

class UserRegisterAPIView(generics.GenericAPIView):

	serializer_class  = UserRegisterSerializer

	def post(self,request,*args,**kwargs):
		serializer = self.get_serializer(data = request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		return Response(serializer.data,status = status.HTTP_201_CREATED)

class UserLoginAPIView(generics.GenericAPIView):

	serializer_class = LoginSerializer

	def post(self,request,*args,**kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data
		# print(RefreshToken.for_user(user))
		# print("#######",AccessToken.for_user(user))
		access_token = AccessToken.for_user(user)
		refersh_token = RefreshToken.for_user(user)

		return Response({
			"user":UserSerializer(user,context=self.get_serializer_context()).data,
			"access_token": str(access_token),
			"refersh_token": str(refersh_token)
			})
	




