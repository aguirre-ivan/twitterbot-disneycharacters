import tweepy, time
from credentials import *
from image_managment import create_image, remove_image
from disney_characters import get_random_character_id, get_tweet_text, get_disney_character_url_image

IMAGE_NAME = "image.png"
WAITING_TIME = 28800 # secs = 8 hours


def twitter_api_setup():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    return api


def create_tweet(bot):
    id_character = get_random_character_id()

    tweet = get_tweet_text(id_character)

    url_image = get_disney_character_url_image(id_character)
    create_image(url_image, IMAGE_NAME)
    media = bot.media_upload(IMAGE_NAME)

    bot.update_status(tweet, media_ids=[media.media_id])

    remove_image(IMAGE_NAME)


if __name__ == '__main__':
    # Setup twitter bot API
    bot = twitter_api_setup()

    create_tweet(bot)

    time.sleep(WAITING_TIME)