from distutils import text_file
from pyexpat import model
from django.db import models
from account.models import UserProfile

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title