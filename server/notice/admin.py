from django.contrib import admin
from .models import Notice

# Register your models here.
class NoticeAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'start_date', 'end_date', 'status', 'priority')
	search_fields = ['title', 'description', 'priority']

admin.site.register(Notice, NoticeAdmin)