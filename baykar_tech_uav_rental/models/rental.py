from django.db import models
from django.contrib.auth.models import User
from .uav import UAV
from autoslug import AutoSlugField


class Rental(models.Model):
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = AutoSlugField(unique=True, populate_from='generate_slug')

    def generate_slug(self):
        return f"{self.user.username}-{self.uav.brand}-{self.uav.model}-rental"

    def __str__(self):
        return f"Rental of {self.uav.brand} {self.uav.model} by {self.user.username}"
