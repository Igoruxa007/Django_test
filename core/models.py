from __future__ import annotations

from typing import Any

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    h1 = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    slug = models.SlugField(default="")
    description = RichTextUploadingField()
    content = RichTextUploadingField()
    created_at = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class BooksAuthor(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(BooksAuthor, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.title
