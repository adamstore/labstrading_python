from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

# search mode remove it if all doesn't worked
class Search(models.Model):
    title = models.CharField(max_length=200 , null=False , db_index=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

# comment section
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ("date_posted",)
    def __str__(self):
        return f'Comment By {self.name}'