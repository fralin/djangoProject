from django.contrib import admin
from .models import Dive, Site, Diver

# Register your models here.
@admin.register(Diver)
class DiverAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birth_date', 'level')

@admin.register(Site)
class DiveAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'depth')
    search_fields = ('name', 'depth')

@admin.register(Dive)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('date', 'site', 'nbPlaces')
    search_fields = ('date', 'site__name', 'nbPlaces')

