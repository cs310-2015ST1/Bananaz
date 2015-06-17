from django.contrib import admin
from .models import *
from .forms import AccountForm

class FoodTreeInline(admin.TabularInline):
    model = FoodTree

class GardenAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')
    inlines = [FoodTreeInline]
    search_fields = ['name']

class UserAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Garden, GardenAdmin)
admin.site.register(User, UserAdmin)

#twitterauth
class AccountAdmin(admin.ModelAdmin):
	list_display = ["__str__", "timestamp", "updated"]
	# class Meta:
	# 	model = Account
	form = AccountForm

admin.site.register(Account, AccountAdmin)
