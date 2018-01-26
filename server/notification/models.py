from django.db import models
from appProfile.models import Profile
from django.contrib.postgres.fields import JSONField

temp_affected_user = {}
temp_user = {}
temp_user['id'] = 1
temp_affected_user['user'] = [temp_user]

# Create your models here.
class Notification(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(
			Profile,
			on_delete=models.CASCADE,
		)
	image = models.ImageField(upload_to='uploads/notifications/', blank=True)
	title = models.CharField(max_length=32)
	description = models.CharField(max_length=256)
	affected_users = JSONField(default = temp_affected_user)