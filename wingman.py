import time

import tweepy
from config import create_api


def main():
    api = create_api()

def wingman(api):
    user = api.user_timeline(user_id = "307187231", count = 1)
    print(user)
    return user

if __name__ == "__main__":
    main()
