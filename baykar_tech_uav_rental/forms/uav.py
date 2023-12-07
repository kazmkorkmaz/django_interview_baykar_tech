from django import forms
from ..models import UAV, Category


class UAVForm(forms.ModelForm):
    class Meta:
        model = UAV
        fields = ['brand', 'model', 'weight', 'category']

    category = forms.ModelChoiceField(queryset=Category.objects.all())
