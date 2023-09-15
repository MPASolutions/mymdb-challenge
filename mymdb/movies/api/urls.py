from django.urls import path
from movies.api.views import CharacterCreateAPIView, CharacterDetailAPIView, MovieCreateAPIView, MovieDetailAPIView

urlpatterns = [
    path("characters/",
        CharacterCreateAPIView.as_view(),
        name="characters-list"),

    path("character/<int:pk>/",
        CharacterDetailAPIView.as_view(),
        name="character-detail"),
    path("movies/",
        MovieCreateAPIView.as_view(),
        name="movies-list"),

    path("movie/<int:pk>/",
        MovieDetailAPIView.as_view(),
        name="movie-detail")
]