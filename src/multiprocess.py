import tweet_listener
import tweet_preprocessor
import tweet_processor
import tweepy
from tweet_listener import MyListener
from tweepy import OAuthHandler
import json
from tweepy import Stream
import time
import math

if __name__ == "__main__":
	open('python.json', 'w').close()
	
	twitter_stream = Stream(tweet_listener.auth, MyListener())
	twitter_stream.filter(track=["trump"], async=True)
	
	tweet_list = []
	
	#geo_data = {
	#	"type": "FeatureCollection", "features": []
	#	}
	
	print("Stream has started")
	
	time.sleep(2)
	
	var = len(tweet_listener.alltweets)
	print(var)
	x = 0

	while x < var:
		thetweet = tweet_listener.alltweets[x]
		try:
			tweet_text = thetweet['text'].encode('ascii','ignore').lower()
			preprocessed = tweet_preprocessor.preprocess(tweet_text)
			tweet_list.append(preprocessed)
			tweet_processor.count(preprocessed)
			tweet_processor.hash_count(preprocessed)
		except KeyError as e:
			print("Error fetching text")
		del tweet_listener.alltweets[x]
		var = len(tweet_listener.alltweets)
		print(tweet_processor.count_all.most_common(5))
		speed = math.exp((-1/6)*(0.1+var))
		time.sleep(speed)
		
	print("The loop has ended")
	