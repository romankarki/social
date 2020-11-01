from django.urls import path
from .views import test1,PostListCreate,PostRetrieveUpdateDestroy

urlpatterns = [
    path("test/",test1,name="TestAPI"),
    path("posts/",PostListCreate.as_view(),name="ListCreatePosts"),
    path("posts/<int:pk>",PostRetrieveUpdateDestroy.as_view(),name="RetrieveUpdateDestroy"),   
]
