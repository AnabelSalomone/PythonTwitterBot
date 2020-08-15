import tweepy
from decouple import config

CONSUMER_KEY = config("CONSUMER_KEY")
CONSUMER_SECRET = config("CONSUMER_SECRET")
ACCESS_TOKEN = config("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = config("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

API = tweepy.API(auth)

get_mentions = API.mentions_timeline()

# trick to get a dict from the class obj
# get_mentions[0].__dict__.keys()
# I personally checked for a a JSON validator

for mention in get_mentions:
    print(mention.text)
    print(mention.user.screen_name)


