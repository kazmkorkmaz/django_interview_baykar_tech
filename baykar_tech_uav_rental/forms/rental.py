from django import forms
from django.forms import DateTimeInput
from ..models.rental import Rental
from django.core.exceptions import ValidationError


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['uav', 'start_date', 'end_date', 'user']
        widgets = {
            'start_date': DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise ValidationError(
                "Start date cannot be greater than end date.")

        return cleaned_data
