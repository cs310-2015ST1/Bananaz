from django.contrib import admin
from .models import *

class FoodTreeInline(admin.TabularInline):
    model = FoodTree

class GardenAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')
    inlines = [FoodTreeInline]
    search_fields = ['name']

admin.site.register(Garden, GardenAdmin)