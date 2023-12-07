from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class Category(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_categories')
    slug = AutoSlugField(unique=True, populate_from='generate_slug')

    def generate_slug(self):
        return f"{self.name}"

    def __str__(self):
        return self.name
