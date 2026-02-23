from django.db import models
from core.models import Category


class Movies(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    poster = models.ImageField(upload_to='posters/')
    media = models.FileField(upload_to='media/')
    category = models.ManyToManyField(Category, related_name='movies')
    year = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Movies"
        ordering = ['year', 'name']
