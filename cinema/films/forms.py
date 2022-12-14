from django import forms
from django.core.exceptions import ValidationError

from .models import Category, Films
import re


class FilmsForm(forms.ModelForm):
    class Meta:
        model = Films
        fields = ['title', 'content', 'directed_by', 'starring', 'release_date', 'running_time', 'age', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'row': 5}),
            'directed_by': forms.TextInput(attrs={'class': 'form-control'}),
            'starring': forms.TextInput(attrs={'class': 'form-control'}),
            'release_date': forms.TextInput(attrs={'class': 'form-control'}),
            'running_time': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'max_value': 18, 'min_value': 0, 'step_size': 6}),

            'category': forms.Select(attrs={'class': 'form-control', 'empty_label': 'Выберите категорию'}),

        }

        def clean_title(self):
            title = self.cleaned_data['title']
            if re.match(r'\d', title):
                raise ValidationError('Наименование не должно начинаться из цифры')
            return title
