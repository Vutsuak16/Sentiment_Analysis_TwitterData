__name__ = "vutsuak"

import tweepy

ACCESS_TOKEN = '2309050262-YxLP1tfqWQrWc1blVyH8jvuxbJ2fPZCPwb0L4Sl'
ACCESS_SECRET = 'eK2IBq7PqyI2iisqdw5ouppkJJCE02OSXG0AQpDog0uZR'
CONSUMER_KEY = 'McCLzJjS7kc1aD0dCYLsUMTme'
CONSUMER_SECRET = '7suZUiu1OUIo1TUpiiyHPDLNo8fWMkjf7d6N9zBCLKaX3JLwjb'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)
'''following = []
keyword = raw_input("enter a keyword")  # takes only one keyword for the  time being
keyword = "#" + keyword
for user in tweepy.Cursor(api.friends, screen_name="kaustuv deolal").items():
    following.append((str(user.screen_name)))


ct = 5 #only for 5 tweets
for tweet in tweepy.Cursor(api.search, q=keyword).items():
    if ct == 0:
        break
    try:
        if tweet.user.screen_name not in following:
                api.create_friendship(tweet.user.id)
                api.create_favorite(tweet.id)
    except:
        pass

    ct -= 1
'''