from bs4 import BeautifulSoup
import sys
import urllib
import requests
from googlesearch import search
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from textstat.textstat import textstatistics,legacy_round
from nltk.corpus import stopwords
import textstat
from PyPDF2 import PdfFileReader
