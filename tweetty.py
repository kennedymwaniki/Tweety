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


# bot that loves a tweet based on certain words
#  search keywords (python)
search_string = "python"
number_of_Tweets = 2

for tweet in tweepy.Cursor(api.search_tweets, search_string).items(number_of_Tweets):
    try:
        tweet.favorite()
        # tweet.retweet() -> retweets based on a keyword
        print("I liked this tweet")
    except tweepy.errors.TweepyException as e:
        print(e.reason)
    except StopIteration:
        break


# get list of followers and follow based on the name
# for follower in handle_limit(tweepy.Cursor(api.get_followers()).items()):
#     if follower.name == "enter the followers name/profile name":
#         follower.follow()
#         break
#     print(follower)

# for this to work you need the basic x plan which is 100$
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
