from django.db import models
from django.utils import timezone


class Post(models.Model):
    post_title = models.CharField(max_length=30)
    body = models.CharField(max_length=280)
    date = models.DateTimeField(default=timezone.now)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    results = models.IntegerField(default=0)
    boast_or_roast = models.BooleanField(default=False, help_text="boast if clicked")

    def __str__(self):
        return self.post_title


def results(self):
    return (self.upvotes - self.downvotes)