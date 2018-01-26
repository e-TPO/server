from django.contrib import admin
from .models import Profile,  CompanyProfile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('roll_no', 'user', 'avatar')
	search_fields = ['roll_no', 'bio']
	readonly_fields = ('avatar',)

class CompanyProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'user', 'avatar', 'description')
	search_fields = ['id', 'name', 'description']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(CompanyProfile, CompanyProfileAdmin)