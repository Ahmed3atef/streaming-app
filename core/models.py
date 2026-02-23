from django.db import models


class Category(models.Model):
    CATEGORIES = [
        ('a', 'Action'),
        ('c', 'Comedy'),
        ('d', 'Drama'),
        ('h', 'Horror'),
        ('r', 'Romance'),
        ('s', 'Sci-Fi'),
        ('t', 'Thriller'),
        ('f', 'Fantasy'),
    ]
    name = models.CharField(max_length=1, choices=CATEGORIES, unique=True)

    def __str__(self):
        return dict(self.CATEGORIES).get(self.name, "None")

    class Meta:
        verbose_name_plural = "Categories"
