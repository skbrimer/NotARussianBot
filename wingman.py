import settings
import tweepy

auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
auth.set_access_token(settings.access_token, settings.access_token_secret)
api = tweepy.API(auth)

user = api.get_user("Andrewdexter1")
print(user)
