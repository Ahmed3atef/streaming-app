from django.urls import path
from . import views

urlpatterns = [
    path('series/',               views.SeriesListView.as_view(),
         name='series_list'),
    path('series/<int:pk>/',      views.SeriesDetailView.as_view(),
         name='series_detail'),
    path('episode/<int:pk>/',     views.EpisodeDetailView.as_view(),
         name='episode_detail'),
]
