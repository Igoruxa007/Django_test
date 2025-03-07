from __future__ import annotations

from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet
from .views import TodoViewSet, BookViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('todo', TodoViewSet, 'todo')
router.register('book', BookViewSet, 'book')

urlpatterns = [
    path('', include(router.urls)),
]
