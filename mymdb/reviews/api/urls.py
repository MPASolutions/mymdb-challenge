from django.urls import path
from reviews.api.views import ReviewCreateAPIView, ReviewDetailAPIView

urlpatterns = [
    path("reviews/",
        ReviewCreateAPIView.as_view(),
        name="People-list"),

    path("review/<int:pk>/",
        ReviewDetailAPIView.as_view(),
        name="job-detail")
]