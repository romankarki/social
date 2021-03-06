from django.shortcuts import render
from .serializers import PostSerializer,PostCommentReactionSerializer, PostCreateSerializer
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework import generics
from .models import Post
from .permissions import ReadOnly,IsAuthor

# Create your views here.

def test1(self):
    """
    Just for testing purpose
    """
    return  JsonResponse({"message":"Hello, Welcome to my API!"})



class PostListCreate(generics.ListCreateAPIView):
    """
    Responsible for creating  a new post 
    And, Also for listing all the created Posts
    with nested output of reactions and comments
    associated to each respective post
    """
    
    permission_classes = [
         permissions.IsAuthenticated,
    ]
    queryset = Post.objects.all()
    #serializer_class = PostCommentReactionSerializer

    def get_serializer_class(self,*args,**kwargs):
        if self.request.method == 'GET':
            return PostCommentReactionSerializer
        elif self.request.method == 'POST':
            return PostCreateSerializer
        return PostCreateSerializer






class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    posts/id/
    update: update existing data
    delete: delete that specific post
    retrieve: get that specific post
    """
    permission_classes = [
         #permissions.IsAuthenticated,
         IsAuthor,
        
    ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    




