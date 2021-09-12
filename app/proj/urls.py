from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from core.views import api_root


urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),
    path(
        "api/chapters/",
        include(("chapter.urls", "chapter"), namespace="chapter"),
    ),
    path(
        "api/coupons/",
        include(("coupon.urls", "coupon"), namespace="coupon"),
    ),
    path(
        "api/doubts/",
        include(("doubt.urls", "doubt"), namespace="doubt"),
    ),
    path(
        "api/orders/",
        include(("order.urls", "order"), namespace="order"),
    ),
    path(
        "api/reviews/",
        include(("review.urls", "review"), namespace="review"),
    ),
    path(
        "api/courses/",
        include(("course.urls", "course"), namespace="course"),
    ),
    path(
        "api/",
        api_root,
        name="api-root",
    ),
    path(
        "",
        api_root,
        name="root",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
