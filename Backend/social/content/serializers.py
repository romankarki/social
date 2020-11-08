from .models import Post,Comment,Reaction
from rest_framework import serializers
from accounts.serializers import UserSerializer,UserShowSerializer


class PostSerializer(serializers.ModelSerializer):

	user = UserSerializer()
	class Meta:
		model = Post
		fields="__all__"

class CommentSerializer(serializers.ModelSerializer):

	author_of_comment = UserShowSerializer()

	class Meta:
		model = Comment
		fields= "__all__"

class ReactionSerializer(serializers.ModelSerializer):

	author_of_reaction = UserShowSerializer()

	class Meta:
		model = Reaction
		fields = "__all__"

class PostCommentReactionSerializer(serializers.ModelSerializer):

	comments = serializers.SerializerMethodField() #for appending comments associated to a post as a field
	reactions = serializers.SerializerMethodField()# for appending reactions associated to a post as a filed

	author_of_post = UserSerializer()
	class Meta:
		model = Post
		fields = "__all__"

	def get_comments(self,obj):
		comment_qs = Comment.objects.filter(post=obj)
		serialized_data = CommentSerializer(comment_qs,many=True).data
		return serialized_data

	def get_reactions(self,obj):
		reactions_qs = Reaction.objects.filter(post=obj)
		serialized_data = ReactionSerializer(reactions_qs,many=True).data
		return serialized_data