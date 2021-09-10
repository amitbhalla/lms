from django.contrib import admin

from .models import Category, Course


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title",),
    }
    list_display = (
        "id",
        "title",
        "slug",
        "created_date",
        "modified_date",
    )
    list_display_links = (
        "id",
        "title",
        "slug",
    )
    list_filter = [
        "title",
    ]
    ordering = [
        "-created_date",
    ]
    readonly_fields = (
        "id",
        "created_date",
        "modified_date",
    )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("title",),
    }
    list_display = (
        "id",
        "title",
        "slug",
        "instructor",
        "language",
        "price",
        "discount",
        "duration",
        "created_date",
        "modified_date",
    )
    list_display_links = (
        "id",
        "title",
        "slug",
    )
    list_editable = [
        "price",
        "discount",
    ]
    list_filter = [
        "title",
        "language",
        "price",
        "discount",
        "duration",
    ]
    ordering = [
        "-created_date",
    ]
    readonly_fields = (
        "id",
        "created_date",
        "modified_date",
    )
