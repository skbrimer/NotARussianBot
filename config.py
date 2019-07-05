import tweepy
import settings

def create_api():
        consumer_key = settings.consumer_key
        consumer_secret = settings.consumer_secret
        access_token = settings.access_token
        access_token_secret = settings.access_token_secret

        auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
        auth.set_access_token(settings.access_token, settings.access_token_secret)

        api = tweepy.API(auth, wait_on_rate_limit = True,
                            wait_on_rate_limit_notify = True)
        try:
            api.verify_credentials()
            print("API A O.K.")
        except:
            print("Crap, API NO GO")
        return api
