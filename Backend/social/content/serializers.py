from .models import Post,Comment,Reaction
from rest_framework import serializers
from accounts.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):

	user = UserSerializer()
	class Meta:
		model = Post
		fields="__all__"
		
