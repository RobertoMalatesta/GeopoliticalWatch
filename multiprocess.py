import tweet_listener
import tweet_preprocessor
import tweepy
from tweet_listener import MyListener
from tweepy import OAuthHandler
import json
from tweepy import Stream
import time

if __name__ == "__main__":
	open('python.json', 'w').close()
	
	twitter_stream = Stream(tweet_listener.auth, MyListener())
	twitter_stream.filter(track=["economy"], async=True)
	
	tweet_list = []
	
	#geo_data = {
	#	"type": "FeatureCollection", "features": []
	#	}
	
	print("Stream has started")
	
	time.sleep(5)
	
	var = len(tweet_listener.alltweets)
	print(var)
	x = 0

	while x < var:
		thetweet = tweet_listener.alltweets[x]
		try:
			tweet_text = thetweet['text']
			tweet_list.append(tweet_preprocessor.preprocess(tweet_text))
		except KeyError as e:
			print("Error fetching text")
		del tweet_listener.alltweets[x]
		var = len(tweet_listener.alltweets)
		print(var)
		time.sleep(1)
		
	print("The loop has ended")
	