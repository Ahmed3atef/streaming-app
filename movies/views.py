from django.views.generic import ListView, DetailView
from .models import Movies


class MoviesListView(ListView):
    model = Movies
    template_name = 'movies/movies_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        sort = self.request.GET.get('sort', '-year')
        allowed = ['name', '-name', 'year', '-year']
        if sort not in allowed:
            sort = '-year'
        return Movies.objects.all().order_by(sort)


class MovieDetailView(DetailView):
    model = Movies
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.get_object()
        context['related_movies'] = Movies.objects.filter(
            category__in=movie.category.all()
        ).exclude(pk=movie.pk).distinct()[:8]
        return context
