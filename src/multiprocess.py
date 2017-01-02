import tweet_listener
import tweet_processor
import tweepy
from tweet_listener import MyListener
from tweepy import OAuthHandler
import json
from tweepy import Stream
import time

if __name__ == "__main__":
	twitter_stream = Stream(tweet_listener.auth, MyListener())
	twitter_stream.filter(follow=['25073877'], async=True)
	
	tweet_list = []
	
	print("Stream has started")
	
	time.sleep(3)
	
	var = len(tweet_listener.alltweets)
	print(var)
	x = 0

	while x < var:
		thetweet = tweet_listener.alltweets[x]
		tweet_id = thetweet['user']['id_str']
		if (tweet_id == '25073877') or (thetweet['retweeted'] == 'true'):
			tweet_text = thetweet['text']
			tweet_list.append(preprocess(tweet_text))
		del tweet_listener.alltweets[x]
		print("The loop is still going")
		var = len(tweet_listener.alltweets)
		print(var)
		time.sleep(1)

	print("The loop has ended")
	
