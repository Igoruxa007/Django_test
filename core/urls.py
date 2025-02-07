from __future__ import annotations

from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet
from .views import TodoViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('todo', TodoViewSet, 'todo')

urlpatterns = [
    path('', include(router.urls)),
]
