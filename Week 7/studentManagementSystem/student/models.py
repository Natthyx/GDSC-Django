from typing import Any
from django.db import models
from teacher.models import teacher

# Create your models here.
class student(models.Model):
        name = models.CharField(max_length=200)
        student_id = models.CharField(max_length=200)
        department = models.CharField(max_length=200)
        teacher = models.ForeignKey(teacher, on_delete = models.CASCADE)


    
