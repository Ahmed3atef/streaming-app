from django.views.generic import ListView, DetailView
from .models import Series, Episode


class SeriesListView(ListView):
    model = Series
    template_name = 'series/series_list.html'
    context_object_name = 'series'

    def get_queryset(self):
        sort = self.request.GET.get('sort', '-year')
        allowed = ['name', '-name', 'year', '-year']
        if sort not in allowed:
            sort = '-year'
        return Series.objects.all().order_by(sort)


class SeriesDetailView(DetailView):
    model = Series
    template_name = 'series/series_detail.html'
    context_object_name = 'series'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        series = self.get_object()
        context['total_episodes'] = Episode.objects.filter(
            season__series=series
        ).count()
        context['related_series'] = Series.objects.filter(
            category__in=series.category.all()
        ).exclude(pk=series.pk).distinct()[:8]
        return context


class EpisodeDetailView(DetailView):
    model = Episode
    template_name = 'series/episode_detail.html'
    context_object_name = 'episode'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        episode = self.get_object()
        context['season'] = episode.season
        context['series'] = episode.season.series
        context['next_ep'] = episode.season.episodes.filter(
            number__gt=episode.number
        ).first()
        return context
