from __future__ import annotations

from typing import Any

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    h1 = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = RichTextUploadingField()
    content = RichTextUploadingField()
    # image = models.ImageField()
    created_at = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> Any:
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self) -> Any:
        return self.title
