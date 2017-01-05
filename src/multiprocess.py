import tweet_listener
import tweet_preprocessor
import tweepy
from tweet_listener import MyListener
from tweepy import OAuthHandler
import json
from tweepy import Stream
import time

if __name__ == "__main__":
	twitter_stream = Stream(tweet_listener.auth, MyListener())
	twitter_stream.filter(track=["the", "i", "to", "a", "and", "is", "in", "it", "you",
	 							"of", "for", "on", "my", "that", "at", "with"], async=True)
	
	tweet_list = []
	
	print("Stream has started")
	
	time.sleep(1)
	
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
		time.sleep(0.02)

	print("The loop has ended")
	
