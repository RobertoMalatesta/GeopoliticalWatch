import tweepy
from tweepy import OAuthHandler
import json
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'IbPksuAopoAnSddLjsfklPawH'
consumer_secret = 'p4o0Qjn7ykDC6GJQiH6x7kPcwYQZmmNAci7PRsYsOGAtXUrcoD'
access_token = '3947451821-8DphpVzENu4a1iXJLfy7CNCM4MmqE84hEKHrRiO'
access_secret = 'FEXBjKVg1DkqMAwVrEO8AIyXZKsHukrsqFTLVbr8M1tn5'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

def process_or_store(tweet):
	print(json.dumps(tweet))
	
class MyListener(StreamListener):
	
	def on_data(self, data):
		try:
			with open('python.json', 'a') as f:
				f.write(data)
				return True
		except BaseException as e:
			print("\" Error " + on_data + ": \"" % str(e))
		return True
	
	def on_error(self, status):
		print(status)
		return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#YuleClickBait'])


"""for status in tweepy.Cursor(api.home_timeline).items(10):
	# Process a single status
	process_or_store(status._json)"""