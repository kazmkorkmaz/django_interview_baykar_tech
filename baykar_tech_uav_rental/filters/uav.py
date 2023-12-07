import django_filters
from ..models import UAV
from django import forms
from django.db import models


class UAVFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method='filter_search',
        label='Search',
        widget=forms.TextInput(attrs={'placeholder': 'Search UAVs'}),
    )

    class Meta:
        model = UAV
        fields = ['brand', 'model', 'weight', 'category']

    def filter_search(self, queryset, name, value):
        # Customize this based on your needs
        return queryset.filter(
            models.Q(brand__icontains=value) |
            models.Q(model__icontains=value) |
            models.Q(category__name__icontains=value)
        )
