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

FILE_LAST_SEEN_ID = "last_seen_id.txt"

def retrive_last_seen_id(filename):
    file_read = open(FILE_LAST_SEEN_ID, "r")
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, filename):
    file_write = open(FILE_LAST_SEEN_ID, "w")
    file_write.write(str(last_seen_id))
    file_write.close()
    return

last_seen_id = retrive_last_seen_id(FILE_LAST_SEEN_ID)

mentions = API.mentions_timeline(last_seen_id)

for tweet in reversed(mentions):
    print(tweet.user.screen_name)
    last_seen_id = tweet.id
    store_last_seen_id(last_seen_id, FILE_LAST_SEEN_ID)
    if 'alejoferre' in tweet.user.screen_name.lower():
        print("worked")
        API.update_status("@" + tweet.user.screen_name + " Esto es un tweet bot, estoy haciendo un test en python :)")


