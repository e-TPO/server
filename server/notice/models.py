from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Notice(models.Model):
	PRIORITY_CHOICES = (
		('LOW', 'Normal'),
		('MED', 'Medium'),
		('HIGH', 'High'),
	)
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=32)
	description = models.CharField(max_length=512)
	meta = JSONField(blank=True, null=True)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	status = models.BooleanField(default=False)
	priority = models.CharField(max_length=4, choices=PRIORITY_CHOICES, default='LOW')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)