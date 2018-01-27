from django.shortcuts import render
from gensim.summarization import summarize, keywords
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from string import punctuation
from bs4 import BeautifulSoup
import requests

# Create your views here.
## Remove stopwords

noise_list = set(stopwords.words('english') + list(punctuation) + ["said"])

def techcrunch_scraper(request, url):
	page = requests.get(url)
	soup = BeautifulSoup(url)
	article = soup.find(class_="article-entry text").text
	title = soup.find(class_="alpha tweet-title").text

def remove_noise(text):
	words = word_tokenize(text)
	noise_free_words = [word.lower() for word in words if word.lower() not in noise_list]
	output_text = ' '.join(noise_free_words)
	return output_text

def get_summary(text):
	return summarize(text)

def get_keywords(text):
	text = remove_noise(text)
	words = word_tokenize(text)
	text = [word.lower() for word in words if word.lower() not in noise_list]
	output_text = ' '.join(text)
	return keywords(output_text, split=True, pos_filter=('NN'))