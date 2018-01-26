from django.contrib import admin
from .models import Notification

# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
	lisy_display = ('id', 'user', 'title')
	search_fields = ['id', 'user', 'title']

admin.site.register(Notification, NotificationAdmin)