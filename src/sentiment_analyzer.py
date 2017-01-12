import sentiment_trainer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json

divide = 1

nums = [[] for _ in range(4)]

averages = {'compound': 0, 'neg': 0, 'neu': 0, 'pos': 0}
numbers = {'positive': 0, 'negative': 0}

def analyze(text):
	global divide
	category = 0
	sid = SentimentIntensityAnalyzer()
	ss = sid.polarity_scores(text)
	for k in sorted(ss):
		nums[category].append(ss[k])
		averages[k] = sum(nums[category]) / divide
		print('average {0}: {1}, '.format(k, averages[k]))
		category += 1
	if averages['pos'] > averages['neg']:
		numbers['positive'] += 1
	else:
		numbers['negative'] += 1
	with open('data.json', 'w') as w:
		dat = dict(averages)
		dat.update(numbers)
		json_data = json.dumps(dat)
		w.write(json_data)
	divide += 1