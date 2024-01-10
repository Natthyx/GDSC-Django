from typing import Any
from django.db import models

# Create your models here.
class teacher(models.Model):
        name = models.CharField(max_length=200)
        department = models.CharField(max_length=200)
        
