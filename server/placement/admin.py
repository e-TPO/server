from django.contrib import admin
from .models import PlacementSession, PlacementSessionRegistration

# Register your models here.
class PlacementSessionAdmin(admin.ModelAdmin):
	list_display = ('id', 'company', 'description', 'status')
	search_fields = ('id', 'company', 'description')

class PlacementSessionRegistrationAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'placementSession', 'currentStatus')
	search_fields = ('id', 'user', 'placementSession', 'currentStatus')

admin.site.register(PlacementSession, PlacementSessionAdmin)
admin.site.register(PlacementSessionRegistration, PlacementSessionRegistrationAdmin)