from __future__ import annotations

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Post
from .models import Todo, Book


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
    )

    class Meta:
        model = Post
        fields = (
            'id', 'h1', 'title', 'slug', 'description',
            'content', 'created_at', 'author',
        )
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
