from django.db import models
from django.contrib.auth.models import User
from .category import Category
from autoslug import AutoSlugField


class UAV(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    weight = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_uavs')
    slug = AutoSlugField(unique=True, populate_from='generate_slug')

    def generate_slug(self):
        return f"{self.brand}-{self.model}-rental"

    def __str__(self):
        return f"{self.brand} {self.model} - {self.category.name}"
