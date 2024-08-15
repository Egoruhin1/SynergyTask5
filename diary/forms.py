# diary/forms.py

from django import forms
from .models import Travel

class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = [
            'location', 
            'latitude', 
            'longitude', 
            'image', 
            'cost', 
            'cultural_heritage_sites', 
            'places_to_visit', 
            'convenience_rating', 
            'safety_rating', 
            'population_density_rating', 
            'vegetation_rating'
        ]

        widgets = {
            'cultural_heritage_sites': forms.Textarea(attrs={'rows': 4}),
            'places_to_visit': forms.Textarea(attrs={'rows': 4}),
            'convenience_rating': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'safety_rating': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'population_density_rating': forms.NumberInput(attrs={'min': 1, 'max': 10}),
            'vegetation_rating': forms.NumberInput(attrs={'min': 1, 'max': 10}),
        }
