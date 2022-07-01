from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import pagination
from .serializers import PostSerializer
from .serializers import TodoSerializer
from .models import Post
from .models import Todo
from rest_framework.response import Response


class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    ordering = 'created_at'


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberSetPagination


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoSerializer
