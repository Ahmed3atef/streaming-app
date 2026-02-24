from django.views.generic import TemplateView, ListView, DetailView
from movies.models import Movies
from series.models import Series
from .models import Category


class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured'] = Movies.objects.order_by('-year').first()
        context['trending_movies'] = Movies.objects.order_by('-year')[:12]
        context['popular_series'] = Series.objects.order_by('-year')[:6]
        context['categories'] = Category.objects.all()
        return context


class SearchView(TemplateView):
    template_name = 'core/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '').strip()
        movies = Movies.objects.filter(
            name__icontains=query) if query else Movies.objects.none()
        series = Series.objects.filter(
            name__icontains=query) if query else Series.objects.none()
        context['query'] = query
        context['movies'] = movies
        context['series'] = series
        context['total_results'] = movies.count() + series.count()
        context['popular_movies'] = Movies.objects.order_by('-year')[:12]
        return context


class CategoriesView(ListView):
    model = Category
    template_name = 'category/browse.html'
    context_object_name = 'all_categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_movies'] = Movies.objects.all().order_by('-year')
        context['all_series'] = Series.objects.all().order_by('-year')
        context['active_category'] = None
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category/browse.html'
    context_object_name = 'active_category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context['all_categories'] = Category.objects.all()
        context['movies'] = category.movies.all().order_by('-year')
        context['series'] = category.series.all().order_by('-year')
        return context
