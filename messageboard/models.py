from distutils import text_file
from pyexpat import model
from django.db import models

# Create your models here.
class Messages(models.Model):
    text: models.TextField(max_length=500)
    auther: models.TextField(max_length=50)