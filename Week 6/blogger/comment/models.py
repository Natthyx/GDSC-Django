from django.db import models
from blog.models import Post

class Comment(models.Model):
    user = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    def __str__(self):
        return f"{self.user} - {self.content}"