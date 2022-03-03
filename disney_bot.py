# DESCRIPTION:
# A twitter bot that tweets random Disney characters with their information (films, TV shows, videogames)
# Format tweet:
# "character name"
# Films: "character films" 
# TV shows: "character TV shows 
# Videogames: "character videogames" 
# "character image"

# WRITTEN BY:
# Aguirre Iván Gonzalo - github.com/aguirre-ivan

# USAGE:
# Setup credentials.py and run disney_bot.py
# $ python disney_bot.py


import tweepy, time
from credentials import *
from image_managment import create_image, remove_image
from disney_characters import get_random_disney_character, INVALID_URL_IMAGE

IMAGE_NAME = "image.png"
WAITING_TIME = 28800 # secs = 8 hours


def twitter_api_setup():
    """
    Authenticate and access using credentials.py keys

    Returns:
        API access
    """
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    return api


def create_tweet(bot):
    """
    Tweet a random Disney character

    Args:
        bot (API access): from twitter_api_setup()

    Returns:
        None
    """
    character_tweet_text, url_image = get_random_disney_character()

    if url_image != INVALID_URL_IMAGE:
        create_image(url_image, IMAGE_NAME)
        media = bot.media_upload(IMAGE_NAME)

        bot.update_status(character_tweet_text, media_ids=[media.media_id])

        remove_image(IMAGE_NAME)
    else:
        bot.update_status(character_tweet_text)


if __name__ == '__main__':
    bot = twitter_api_setup()

    while(True):
        create_tweet(bot)

        time.sleep(WAITING_TIME)