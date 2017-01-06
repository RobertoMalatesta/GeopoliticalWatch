import json
import operator
from collections import Counter
from nltk.corpus import stopwords
import string

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', 'RT', 'trump', 'trump\'s', 'amp']

count_all = Counter()

def count(word_list):
	terms_all = [term for term in word_list if term not in stop]
	count_all.update(terms_all)
