import random
import tweepy
import settings


auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret)
auth.set_access_token(settings.access_token, settings.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True,
                    wait_on_rate_limit_notify = True)

Messages = ["You got this Sugar Bear",
    "That is a gun in my pocket, but I am happy to see you.",
    "Will you be my Kirsten Dunst?",
    "Put on your positive pants Sugar Bear",
    "Drink some coffee, put on some gansta rap and handle it",
    "Oh, yes you certainly fucking can",
    "Chin up princess or the crown slip",
    "It’s just a flesh wound",
    "I learned a long time ago that worrying is like a rocking chair. It gives you something to do but it doesn’t get you anywhere"]

user_id = "AndrewDexter1"
message = random.choice(Messages)
api.update_status(f"@{user_id}, {message}")
