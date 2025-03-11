from .models import Movie
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, URLInput

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'title_original', 'year_start', 'year_end', 'categories', 'rating', 'description', 'countries', 'url', 'date_now']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'title',
            }),
            'title_original': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'title_original',
            }),
            'year_start': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'year_start',
            }),
            'year_end': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'year_end',
            }),
            'categories': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'categories',
            }),
            'rating': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'rating',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'description',
            }),
            'countries': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'countries',
            }),
            'url': URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'url',
            }),
            'date_now': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'date_now',
                'type': 'datetime-local',
            }),
        }