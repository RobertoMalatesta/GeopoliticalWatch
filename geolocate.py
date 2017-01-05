from geopy.geocoders import Nominatim

geo_data = {
	"type": "FeatureCollection", "features": []
	}

def geoLocate(tweet):
	try:
		geolocator = Nominatim()
		loc = tweet['user']['location']
		location = geolocator.geocode(loc)
		try:
			coordinates = [location.latitude, location.longitude]
			geo_json_feature = {
				"type": "Feature",
				"geometry": coordinates,
				"properties": {
					"text": tweet['text'],
					"created_at": tweet['created_at']
				}
			}
			return geo_json_feature
		except AttributeError as f:
			print("No coordinates available")
			return None
	except KeyError as e:
		print("Tweet is some shit")
		return None