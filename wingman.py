import random
import tweepy
from config import create_api

Messages = ["You got this Sugar Bear",
    "That is a gun in my pocket, but I am happy to see you.",
    "Will you be my Kirsten Dunst?",
    "Put on your positive pants Sugar Bear",
    "Drink some coffee, put on some gansta rap and handle it",
    "Oh, yes you certainly fucking can",
    "Chin up princess or the crown slip",
    "It’s just a flesh wound",
    "I learned a long time ago that worrying is like a rocking chair. It gives you something to do but it doesn’t get you anywhere"]

def wingman(api):
    user_id = "307187231"
    message = random.choice(Messages)
    api.update_status(f"@{user_id}, {message}")


def main():
    api = create_api()


if __name__ == "__main__":
    main()
