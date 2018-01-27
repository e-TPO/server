from django.db import models
from gensim.summarization import summarize, keywords
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from string import punctuation
from bs4 import BeautifulSoup
import requests
import nltk

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
	title = models.CharField(max_length = 255, null=True, blank=True)
	author = models.CharField(max_length = 255, blank=True, null=True)
	body = models.TextField(null=True, blank=True)
	summary = models.TextField(blank=True, null=True)
	image_url = models.URLField(max_length = 255, blank=True, null=True)
	url = models.URLField(max_length=255)
	status = models.CharField(max_length=3, choices=ARTICLE_STATUS, default=ADD)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return  self.title  

	def __unicode__(self):
		return self.title

	def save(self, *args, **kwargs):
		page = requests.get(self.url)
		print(page.content)
		noise_list = set(stopwords.words('english') + list(punctuation) + ["said"])
		soup = BeautifulSoup(page.content, "html.parser")
		article = soup.find(class_="entry-content").text
		self.title = soup.find(class_="entry-title").text
		self.body = article
		self.status = SUM
		self.summary = summarize(self.title + article)
		super(Article, self).save(*args, **kwargs)