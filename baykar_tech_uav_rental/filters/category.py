import django_filters
from django import forms
from ..models import Category


class CategoryFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method='filter_search',
        label='Search',
        widget=forms.TextInput(attrs={'placeholder': 'Search categories'}),
    )

    class Meta:
        model = Category
        fields = ['name', 'created_by']

    def filter_search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)
