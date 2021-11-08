from django.contrib.auth.models import User
from django.db import models


"""Post category Model"""
class Category(models.Model):
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.cat_name}'


"""Model for Posts on the blog"""
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post_content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    post_image = models.ImageField(upload_to='post_images')
    post_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.title}'


""" Model for Post Comments """
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'