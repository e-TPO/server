from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	fcm_token = models.TextField(max_length=32, blank=True)
	roll_no = models.IntegerField(default=00000000)
	avatar = models.ImageField(upload_to='uploads/avatar/user/', blank=True)
	resume = models.FileField(upload_to='uploads/resume/', blank=True)
	social = JSONField(blank=True, null=True)
	projects = JSONField(blank=True, null=True)
	achievements = JSONField(blank=True, null=True)
	contact_number = models.CharField(blank=True, null=True, max_length=10)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def image_tag(self):
		return make_safe('<img src="%s" width="150" height="150" />' % (self.avatar))
	image_tag.short_description = 'Image'
	image_tag.allow_tags = True

	def __str__(self):
		return  str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile. objects. create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()

class CompanyProfile(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.TextField(max_length=32, default='e-TPO')
	description = models.TextField(max_length=500)
	avatar = models.ImageField(upload_to='uploads/avatar/company/')
	status = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return  str(self.name)