import uuid
from django.db import models

from course.models import Course


CHAPTER_CHOICES = (
    ("text", "Text Chapter"),
    ("heading", "Heading Chapter"),
    ("video", "Video Chapter"),
    ("link", "Link Chapter"),
)


class Chapter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="chapters"
    )
    chapter_type = models.CharField(max_length=255, choices=CHAPTER_CHOICES)
    index = models.IntegerField()
    parent_chapter = models.ForeignKey(
        "Chapter",
        on_delete=models.SET_NULL,
        related_name="childchapters",
        null=True,
        blank=True,
    )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.chapter_type
