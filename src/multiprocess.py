from tweet_listener import *
from tweet_processor import *

if __name__ == "__main__":
	twitter_stream = Stream(auth, MyListener())
	twitter_stream.filter(follow=['25073877'], async=True)

	tweet_list = []
	tweetcount = 0
	count = 0
	while True:
		f = open('python.json', 'r')
		line = f.readline()
		for line in f:
			while count < tweetcount:
				json.loads(line)
				count += 1
			trumptweet = json.loads(line)
			tweet_id = trumptweet['user']['id_str']
			tweetcount += 1
			if (tweet_id == '25073877') or (trumptweet['retweeted'] == 'true'):
				tweet_text = trumptweet['text']
				tweet_list.extend(preprocess(tweet_text))
		f.close()
		print(tweet_list)
		print(tweetcount)
