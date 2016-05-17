__name__ = "vutsuak"

import tweepy
import json

ACCESS_TOKEN = '2309050262-YxLP1tfqWQrWc1blVyH8jvuxbJ2fPZCPwb0L4Sl'
ACCESS_SECRET = 'eK2IBq7PqyI2iisqdw5ouppkJJCE02OSXG0AQpDog0uZR'
CONSUMER_KEY = 'McCLzJjS7kc1aD0dCYLsUMTme'
CONSUMER_SECRET = '7suZUiu1OUIo1TUpiiyHPDLNo8fWMkjf7d6N9zBCLKaX3JLwjb'


class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        j= json.loads(data)
        print j['text']
        return True

    def on_error(self, status):
        print status


if __name__ == 'vutsuak':
    # This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    stream = tweepy.Stream(auth, l)

    # This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['bangalore'])
