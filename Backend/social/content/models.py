from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    """
    Scheme  for every possible posts that a user can create
    """
    caption = models.CharField(max_length=500)
    postedOn = models.DateTimeField(auto_now_add = True) #for a new post only not for updates 
    status = models.CharField(max_length=500)
    photo = models.ImageField( upload_to="posts",blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return (self.caption)

        

class Reaction(models.Model):
    """
    Reactions given to a certain post such as like,dislike,love etc
    """
    user_reaction = [
        ("HAHA","HAHA"),("LOVE","LOVE"),("LIKE","LIKE"),("SAD","SAD"),("ANGRY","ANGRY"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    post_reaction = models.CharField( max_length=50,choices = user_reaction,blank=True,null=True)

    def __str__(self):
        return self.post_reaction
    
    


    

