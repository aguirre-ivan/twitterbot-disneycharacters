import tweepy, time
from credentials import *
from image_managment import create_image, remove_image
from disney_characters import get_random_disney_character

IMAGE_NAME = "image.png"
WAITING_TIME = 28800 # secs = 8 hours


def twitter_api_setup():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    return api


def create_tweet(bot):
    character_info, url_image = get_random_disney_character()

    create_image(url_image, IMAGE_NAME)
    media = bot.media_upload(IMAGE_NAME)

    bot.update_status(character_info, media_ids=[media.media_id])

    remove_image(IMAGE_NAME)


if __name__ == '__main__':
    # Setup twitter bot API
    bot = twitter_api_setup()

    create_tweet(bot)

    time.sleep(WAITING_TIME)