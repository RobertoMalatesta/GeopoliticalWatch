import sentiment_trainer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

divide = 1

nums = [[] for _ in range(4)]

averages = [0, 0, 0, 0]

def analyze(text):
	global divide
	category = 0
	sid = SentimentIntensityAnalyzer()
	ss = sid.polarity_scores(text)
	for k in sorted(ss):
		nums[category].append(ss[k])
		averages[category] = sum(nums[category]) / divide
		print('average {0}: {1}, '.format(k, averages[category]))
		category += 1
	divide += 1
	print()