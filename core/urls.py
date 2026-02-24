from django.urls import path
from . import views

urlpatterns = [
    path('',                 views.HomeView.as_view(),          name='home'),
    path('search/',          views.SearchView.as_view(),        name='search'),
    path('browse/',          views.CategoriesView.as_view(),    name='categories'),
    path('browse/<int:pk>/', views.CategoryDetailView.as_view(),
         name='category_detail'),
]
