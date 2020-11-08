from django.urls import path
from .views import UserRegisterAPIView,UserLoginAPIView

urlpatterns=[
	path("register/",UserRegisterAPIView.as_view(),name="register"),
	path("post/",UserLoginAPIView.as_view(),name="login")
]