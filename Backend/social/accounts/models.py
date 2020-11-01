from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here

class User(AbstractUser):

	full_name = models.CharField(max_length=200)
	profile_picture = models.ImageField(upload_to="profile_pictures",blank=True,null=True)
	address = models.CharField(max_length=100)
