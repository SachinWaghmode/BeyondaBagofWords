from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "czech"
SENTENCES_COUNT = 10

def homepage(request):
	print("inside home")
	return render(request, 'home.html')

def count(request):
	print("inside count")
	URL = request.GET.get('urlvalue')
	
	print(URL)
	url = "https://www.quora.com/What-is-a-blog-post"
	parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
	stemmer = Stemmer(LANGUAGE)
	summarizer = Summarizer(stemmer)
	summarizer.stop_words = get_stop_words(LANGUAGE)
	for sentence in summarizer(parser.document, SENTENCES_COUNT):
		print(sentence)
		
	return render(request, 'count.html', {'sentence': sentence})
	
