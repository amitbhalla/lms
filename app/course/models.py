import os
import uuid
from django.db import models


def course_thumbnail(instance, filename):
    """Generate file path for a resource"""
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join("upload/course/", filename)


def course_resource(instance, filename):
    """Generate file path for a resource"""
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join("upload/course/", filename)


class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=255, null=False)
    slug = models.SlugField(null=False, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["-modified_date"]

    def __str__(self):
        return self.title


class Course(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=255, null=False)
    slug = models.SlugField(null=False, unique=True)
    instructor = models.CharField(max_length=255, null=False)
    language = models.CharField(max_length=255, null=False)
    description = models.TextField()
    tagline = models.CharField(max_length=255, null=False)
    price = models.FloatField(null=False)
    discount = models.FloatField(default=0.0, null=False)
    duration = models.IntegerField(null=False)
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        null=False,
        related_name="courses",
    )
    thumbnail = models.ImageField(upload_to=course_thumbnail)
    resource = models.FileField(upload_to=course_resource)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-modified_date"]

    def __str__(self):
        return self.title


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    tag = models.CharField(max_length=255, null=False)
    slug = models.SlugField(null=False, unique=True)
    course = models.ForeignKey(
        "Course",
        on_delete=models.CASCADE,
        related_name="tags",
    )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-modified_date"]

    def __str__(self):
        return self.tag
