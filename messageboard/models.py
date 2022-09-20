from distutils import text_file
from pyexpat import model
from django.db import models

# Create your models here.
class Messages(models.Model):
    text: models.TextField()
    auther: models.CharField(max_length=50)

    def __str__(self):
        return self.text[:15]