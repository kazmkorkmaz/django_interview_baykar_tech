# filters.py
import django_filters
from ..models.rental import Rental
from django import forms
from django.db import models
from django.forms import DateTimeInput


class RentalFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method='filter_search',
        label='Search',
        widget=forms.TextInput(attrs={'placeholder': 'Search Rentals'}),
    )
    start_date = django_filters.DateFromToRangeFilter(
        label='Start Date',
        widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
    )

    end_date = django_filters.DateFromToRangeFilter(
        label='End Date',
        widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
    )

    class Meta:
        model = Rental
        fields = ['uav', 'start_date', 'end_date', 'user']

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            models.Q(uav__brand__icontains=value) |
            models.Q(uav__model__icontains=value) |
            models.Q(user__username__icontains=value)
        )
