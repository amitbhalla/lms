from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Category, Course, Tag
from .serializers import CategorySerializer, CourseSerializer, TagSerializer
from core.permissions import IsAdminUserOrReadOnly


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategorySlugDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "slug"


class CourseViewSet(ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseSlugDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = "slug"


class TagViewSet(ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TagSlugDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    lookup_field = "slug"
