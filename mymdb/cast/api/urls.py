from django.urls import path
from cast.api.views import PersonCreateAPIView, PersonDetailAPIView

urlpatterns = [
    path("people/",
        PersonCreateAPIView.as_view(),
        name="People-list"),

    path("person/<int:pk>/",
        PersonDetailAPIView.as_view(),
        name="job-detail")
]