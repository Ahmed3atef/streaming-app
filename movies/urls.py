from django.urls import path
from . import views

urlpatterns = [
    path('movies/',          views.MoviesListView.as_view(),  name='movies_list'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
]
