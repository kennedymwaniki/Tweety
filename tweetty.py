import tweepy

import time

auth = tweepy.OAuthHandler('oqV9w4QdJ0pxdKUM5ShrJB9tI', 'pijTDklJWBYtYktuLPRBg3pwpXK2tLjyo8hwYblPQGPPpD4g75')
auth.set_access_token('1834114836231274496-Mhd3vF4bRlXAYnaEFQwcI4CMCHVjNk',
                      'QeOTnX1A7yEyaRQjTfUswlB0eMmgu9yPgBd2snzfN47UE')

api = tweepy.API(auth)

# create a tweepy client object
client = tweepy.Client(consumer_key='oqV9w4QdJ0pxdKUM5ShrJB9tI',
                       consumer_secret='pijTDklJWBYtYktuLPRBg3pwpXK2tLjyo8hwYblPQGPPpD4g75',
                       access_token='1834114836231274496-Mhd3vF4bRlXAYnaEFQwcI4CMCHVjNk',
                       access_token_secret='QeOTnX1A7yEyaRQjTfUswlB0eMmgu9yPgBd2snzfN47UE')

# Get the authenticated user's information
user = client.get_me()


# if we get a rate limit error we pause the application
def handle_limit(cursor):
    try:
        while True:
            yield cursor.next()

    except tweepy.RateLimitError:
        time.sleep(1000)


# bot
for follower in handle_limit(tweepy.Cursor(api.get_followers()).items()):
    print(follower.name)

# for this to work you need the basic x plan which is 100$
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
