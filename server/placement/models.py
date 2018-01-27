from django.db import models
from appProfile.models import CompanyProfile, Profile
from django.contrib.postgres.fields import JSONField

# Create your models here.
temp_requirements = {}
temp_requirements['cpi'] = 5.0
temp_requirements['sem'] = 5


# It will be like
'''
{
	no : 1,
	rounds_detail : 	[
							{
								step : 1,
								title : "Sample round detail",
								description : "Sample Description"
							},
						]
}
'''

temp_round = {}
temp_round_details = {}
temp_round['no'] = 1
temp_round_details['step'] = 1
temp_round_details['title'] = "Sample round detail"
temp_round_details['description'] = "Sample description"
temp_round['rounds_detail'] = [temp_round_details, temp_round_details]

class PlacementSession(models.Model):
	id = models.AutoField(primary_key=True)
	company = models.ForeignKey(
			CompanyProfile,
			on_delete = models.CASCADE
		)
	requirements = JSONField(default=temp_requirements)
	title = models.CharField(max_length=32)
	description = models.CharField(max_length=512)
	rounds = JSONField(default=temp_round)
	status = models.BooleanField(default=False)

	def __str__(self):
		return  str(self.company.name + "=>" + self.title)

temp_status = {}
temp_status['current_status'] = 1
temp_status['description'] = 'Hello World'
class PlacementSessionRegistration(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(
				Profile,
				on_delete=models.CASCADE
			)
	placementSession = models.ForeignKey(
				PlacementSession,
				on_delete=models.CASCADE
			)
	currentStatus = JSONField(blank=True, null=True)
	def save(self, *args, **kwargs):
		if not self.pk:
			temp_status = {}
			temp_status['current_status'] = self.placementSession.rounds['rounds_detail'][0]['step']
			temp_status['description'] = self.placementSession.rounds['rounds_detail'][0]['description']
			print(temp_status)
			self.currentStatus = temp_status
		super(PlacementSessionRegistration, self).save(*args, **kwargs)

	def __str__(self):
		return  str(str(self.user) + "=>" + str(self.placementSession))