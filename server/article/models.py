from django.db import models

# Create your models here.
ADD = 'ADD'
SUM = 'SUM'
OTH = 'OTH'

ARTICLE_STATUS = (
	(ADD, 'Added'),
	(SUM, 'Summarized'),
	(OTH, 'Other'),
)


class Article(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length = 255)
	author = models.CharField(max_length = 255, blank=True, null=True)
	body = models.TextField()
	summary = models.TextField(blank=True, null=True)
	image_url = models.URLField(max_length = 255, blank=True, null=True)
	url = models.URLField(max_length=255)
	status = models.CharField(max_length=3, choices=ARTICLE_STATUS)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return  self.title  

	def __unicode__(self):
		return self.title