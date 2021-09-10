from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),
    path(
        "api/chapters/",
        include("chapter.urls"),
    ),
    path(
        "api/coupons/",
        include("coupon.urls"),
    ),
    path(
        "api/courses/",
        include("course.urls"),
    ),
    path(
        "api/doubts/",
        include("doubt.urls"),
    ),
    path(
        "api/orders/",
        include("order.urls"),
    ),
    path(
        "api/reviews/",
        include("review.urls"),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
