from django.db import models
import datetime
'''
title : char field (max 2048)
content : text field.
is_published : boolean field, default is True.
published_at : datetime field, default is now.
'''
class Post(models.Model):
    title = models.CharField(max_length=2048)
    content =models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=datetime.datetime.now())
    photo = models.ImageField(default='images/default.jpg',upload_to='images/')

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    comment = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)