import json

from accounts.models import User
from accounts.serializers import UserSerializer
from django.test import Client, TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Comment, Post, Reaction
from .serializers import PostSerializer,PostCommentReactionSerializer

client = Client()

# Create your tests here.

class ContentTest(APITestCase):

    def setUp(self):
        """
        creating the necessary datas for futher testing
        """
        user = User.objects.create(full_name="James Bond",address="Kathmandu-03",email="james@bond.com")
        post = Post.objects.create(
            status="hi! I'm james bond!!",
            author_of_post = user
            )
    
    def test_post_get(self):
        """
        testing one of the api for test
        """
        response = client.get(reverse("ListCreatePosts"))
        posts = Post.objects.all()
        data = PostCommentReactionSerializer(posts,many=True)
        self.assertEqual(response.data,data.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


