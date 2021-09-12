from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import status

from .models import Category, Course, Tag
from .serializers import CategorySerializer, CourseSerializer, TagSerializer
from core.permissions import IsAdminUserOrReadOnly


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CategorySerializer
    filterset_fields = ["title", "id", "slug"]
    search_fields = ["title", "id", "slug"]
    queryset = Category.objects.all()


class CategorySlugDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "slug"


class CategoryCoursesView(APIView):
    def get(self, request, category_id):
        try:
            courses = Course.objects.filter(category=Category(pk=category_id))
        except (Course.DoesNotExist, ValidationError):
            error_message = {"category": ["category_id is invalid!"]}
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

        serializer = CourseSerializer(courses, many=True)
        if courses.count() > 0:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"Course": "No courses found with that id."},
                status=status.HTTP_200_OK,
            )


class CourseViewSet(ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = CourseSerializer
    filterset_fields = [
        "title",
        "id",
        "slug",
        "language",
        "price",
        "discount",
        "instructor",
    ]
    search_fields = [
        "title",
        "id",
        "slug",
        "language",
        "price",
        "discount",
    ]
    queryset = Course.objects.filter()

    def get_queryset(self):
        tag = self.request.query_params.get("tag")
        if tag is not None:
            courses = Tag.objects.filter(tag=tag).values_list("course")
            return self.queryset.filter(pk__in=courses)
        return self.queryset

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
    filterset_fields = ["id", "tag"]
    search_fields = ["id", "tag"]
    queryset = Tag.objects.all()


class TagViewSet(ModelViewSet):
    permission_classes = [IsAdminUserOrReadOnly]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    filterset_fields = ["id", "tag"]

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
