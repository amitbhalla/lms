from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(request):
    context = {
        "API Root": {
            "Root": reverse("root", request=request),
            "API Root": reverse("api-root", request=request),
        },
        "Courses App": {
            "Category": {
                "Category List View": reverse(
                    "course:category-list",
                    request=request,
                ),
                "Category Detail View [PK]": reverse(
                    "course:category-detail",
                    request=request,
                    args=[1],
                ),
                "Category Detail View [Slug]": reverse(
                    "course:category-detail-by-slug",
                    request=request,
                    args=["slug-val"],
                ),
                "Category Courses": reverse(
                    "course:category-courses-list",
                    request=request,
                    args=["course-id"],
                ),
            },
            "Course": {
                "Course List View": reverse(
                    "course:course-list",
                    request=request,
                ),
                "Course Detail View [PK]": reverse(
                    "course:course-detail",
                    request=request,
                    args=[1],
                ),
                "Course Detail View [Slug]": reverse(
                    "course:course-detail-by-slug",
                    request=request,
                    args=["slug-val"],
                ),
            },
            "Tag": {
                "Tag List View": reverse(
                    "course:tag-list",
                    request=request,
                ),
                "Tag Detail View [PK]": reverse(
                    "course:tag-detail",
                    request=request,
                    args=[1],
                ),
                "Tag Detail View [Slug]": reverse(
                    "course:tag-detail-by-slug",
                    request=request,
                    args=["slug-val"],
                ),
            },
        },
    }
    return Response(context)
