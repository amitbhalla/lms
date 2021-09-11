from django.urls import path

from .views import CategoryListView, CategoryDetailView

urlpatterns = [
    path(
        "categories/<str:pk>/",
        CategoryDetailView.as_view(),
        name="categories-detailview",
    ),
    path(
        "categories/",
        CategoryListView.as_view(),
        name="categories-listview",
    ),
]
