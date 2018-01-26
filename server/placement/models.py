from django.db import models
from appProfile.models import CompanyProfile
from django.contrib.postgres.fields import JSONField

# Create your models here.
temp_requirements = {}
temp_requirements['cpi'] = 5.0
temp_requirements['sem'] = 5


# It will be like
'''
{
	no : 1,
	rounds_details : 	[
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
temp_round['rounds_details'] = [temp_round_details, temp_round_details]

class PlacementSession(models.Model):
	id = models.AutoField(primary_key=True)
	company = models.ForeignKey(
			'CompanyProfile',
			on_delete = models.CASCADE
		)
	requirements = JSONField(default=temp_requirements)
	title = models.CharField(max_field=32)
	description = models.CharField(max_field=512)
	rounds = JSONField()