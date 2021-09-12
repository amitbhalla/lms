from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import status

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

    def create(self, request, *args, **kwargs):
        course = request.data
        category_id = course.get("category")

        if category_id is None:
            error_message = {
                "category": ["category_id is required."],
            }
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
        try:
            category = Category.objects.get(pk=category_id)
        except (Category.DoesNotExist, ValidationError):
            error_message = {
                "category": ["category_id is not valid."],
            }
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

        context = {
            "request": request,
        }
        serializer = CourseSerializer(data=course, context=context)

        if serializer.is_valid():
            course = Course(**serializer.validated_data, category=category)
            course.save()
            return Response(
                CourseSerializer(course, context=context).data,
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class CourseSlugDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = "slug"


class TagViewSet(ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def create(self, request, *args, **kwargs):
        tag = request.data
        course_id = tag.get("course")

        if course_id is None:
            error_message = {
                "course": ["course_id is required."],
            }
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
        try:
            course = Course.objects.get(pk=course_id)
        except (Course.DoesNotExist, ValidationError):
            error_message = {
                "course": ["course_id is invalid!"],
            }
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

        context = {
            "request": request,
        }
        serializer = TagSerializer(data=tag, context=context)

        if serializer.is_valid():
            tag = Tag(**serializer.validated_data, course=course)
            tag.save()
            return Response(
                TagSerializer(tag, context=context).data,
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


class TagSlugDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    lookup_field = "slug"
