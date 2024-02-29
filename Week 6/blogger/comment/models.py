from django.db import models
from blog.models import Post

class Comment(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=255)
    published_date = models.DateTimeField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.content}'
