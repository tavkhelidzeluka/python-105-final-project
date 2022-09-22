from django.db import models
from account.models import UserProfile
from django.urls import reverse

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("postsite:post_detail", args=[str(self.pk)])


class Comment(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:20]

    def get_absolute_url(self):
        return reverse("postsite:home", args=[str(self.pk)])