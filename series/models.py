from django.db import models
from core.models import Category


class Series(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    poster = models.ImageField(upload_to='series/posters/')
    category = models.ManyToManyField(Category, related_name='series')
    year = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Series"
        ordering = ['year', 'name']


class Season(models.Model):
    series = models.ForeignKey(
        Series, on_delete=models.CASCADE, related_name='seasons')
    number = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.series.name} - Season {self.number}"

    class Meta:
        ordering = ['number']
        # prevent duplicate season numbers per series
        unique_together = ('series', 'number')


class Episode(models.Model):
    season = models.ForeignKey(
        Season, on_delete=models.CASCADE, related_name='episodes')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    number = models.PositiveIntegerField()
    duration = models.DurationField(null=True, blank=True)
    media = models.FileField(upload_to='series/episodes/')
    thumbnail = models.ImageField(
        upload_to='series/thumbnails/', null=True, blank=True)

    def __str__(self):
        return f"{self.season.series.name} - S{self.season.number}E{self.number} - {self.title}"

    class Meta:
        ordering = ['number']
        # prevent duplicate episode numbers per season
        unique_together = ('season', 'number')
