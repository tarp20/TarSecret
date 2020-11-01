from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=100,)
    slug = models.SlugField(unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField( verbose_name="Text")
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL, related_name='posts', blank=True, null=True)

    class Meta:
        ordering = ['-pub_date']
