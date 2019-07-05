import settings
import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
auth.set_access_token(settings.access_token, settings.access_token_secret)

# Create API object
api = tweepy.API(auth)

# Create tweet
api.update_status("@Andrewdexter1, Just saying hi Sugar Bear. #YouAreAwesome")

#user = api.user_timeline("Andrewdexter1")
#print(user)
