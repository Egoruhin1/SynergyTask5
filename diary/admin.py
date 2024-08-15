# diary/admin.py

from django.contrib import admin
from .models import Travel

class TravelAdmin(admin.ModelAdmin):
    list_display = (
        'location', 
        'latitude', 
        'longitude', 
        'cost', 
        'convenience_rating', 
        'safety_rating'
    )

admin.site.register(Travel, TravelAdmin)
