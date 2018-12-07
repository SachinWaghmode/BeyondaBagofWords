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
# SENTENCES_COUNT = 10


def homepage(request):
	return render(request, 'home.html')

def count(request):
	URL = request.GET.get('urlvalue')
	SENTENCES_COUNT = request.GET.get('SENTENCES_COUNT')
	parser = HtmlParser.from_url(URL, Tokenizer(LANGUAGE))
	stemmer = Stemmer(LANGUAGE)
	summarizer = Summarizer(stemmer)
	summarizer.stop_words = get_stop_words(LANGUAGE)
	result = []
	for sentence in summarizer(parser.document, SENTENCES_COUNT):
    		result.append(sentence)

		
	return render(request, 'count.html', {'result': result})
	
