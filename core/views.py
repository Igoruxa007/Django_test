from __future__ import annotations

from rest_framework import pagination
from rest_framework import permissions
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import Post
from .models import Todo, Book, BooksAuthor
from .serializers import PostSerializer
from .serializers import AuthorSerializer
from .serializers import TodoSerializer, BookSerializer


class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    ordering = 'created_at'


@method_decorator(cache_page(60 * 150), name='dispatch')
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberSetPagination


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = TodoSerializer


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.AllowAny]


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = BooksAuthor.objects.all()
    permission_classes = [permissions.AllowAny]
