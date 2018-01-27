from django.db import models
from appProfile.models import Profile

# Create your models here.
# class Skill(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	description = models.CharField(max_length=32)

# class SkillDetail(models.Model):
# 	id = models.AutoField(primary_key=True)
# 	user = models.ForeignKey(
# 			Profile,
# 			on_delete=models.CASCADE
# 		)
# 	skill = models.ForeignKey(
# 			Skill
# 			on_delete=models.CASCADE
# 		)