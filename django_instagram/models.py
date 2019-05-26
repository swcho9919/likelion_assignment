from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    img = models.FileField(null=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()