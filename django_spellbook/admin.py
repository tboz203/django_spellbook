from django.contrib import admin
from django_spellbook.models import Spell

@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
    list_display_links = ['name']
    list_display = [
        'level', 'name', 'school', 'range', 'components', 'duration', 'concentration', 'ritual'
    ]
    search_fields = ['name', 'school', 'description', 'description_high']
    list_filter = ['level', 'concentration', 'ritual', 'favorite']