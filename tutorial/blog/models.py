from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # If a user is deleted, delete the post
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # Will return the url as a string and let the view do the rest
    # Rather than redirect
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
