from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    title = models.TextField(max_length= 100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
