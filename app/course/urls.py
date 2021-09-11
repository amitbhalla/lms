from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet

category_router = DefaultRouter()
category_router.register("", CategoryViewSet, basename="category")


urlpatterns = [
    path(
        "categories/",
        include(category_router.urls),
    ),
]
