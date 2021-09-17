from django.contrib import admin

from .models import Chapter


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "course",
        "chapter_type",
        "index",
        "parent_chapter",
        "created_date",
        "modified_date",
    )
    list_editable = [
        "index",
    ]
    list_display_links = (
        "id",
        "course",
    )
    list_filter = [
        "course",
    ]
    ordering = [
        "-created_date",
    ]
    readonly_fields = (
        "id",
        "created_date",
        "modified_date",
    )
