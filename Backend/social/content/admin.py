from django.contrib import admin
from  .models import Post,Reaction,Comment


# Register your models here.

admin.site.register(Post)
admin.site.register(Reaction)
admin.site.register(Comment)
