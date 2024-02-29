from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/')
    tags = models.CharField(max_length=255)  

    def get_tags_list(self):
        return [tag.strip() for tag in self.tags.split(',')]

    def __str__(self):
        return self.title
