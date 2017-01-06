import json
import operator
from collections import Counter
from nltk.corpus import stopwords
import string

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', 'RT', 'trump', 'trump\'s', 
													'amp', 'https', 'donald', 'president-elect',
													'says']

count_all = Counter()
count_hash = Counter()

def count(word_list):
	terms_all = [term for term in word_list if term not in stop and not term.startswith(('#', '@'))] 
	count_all.update(terms_all)

def hash_count(word_list):
	terms_hash = [term for term in word_list if term.startswith('#')]
	count_hash.update(terms_hash)