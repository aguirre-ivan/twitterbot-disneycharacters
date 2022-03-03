import requests
from random import randint

MAX_CHARACTER_ID = 7526
TWEET_LEN_LIMIT = 280

INVALID_URL_IMAGE = -1
URL_CHARACTER = 'https://api.disneyapi.dev/characters/'


def get_info_in_format(title_info, list_info):
    """
    Returns info in format tweet

    Args:
        title_info (str):
            Title in format tweet
            Example: "TV shows" for tvShows 
        list_info (list):
            List of strings, with the info
            Example: ["film1", "film2"] for Films

    Returns:
        str: Info in format tweet
        If list_info = [], returns ''
    """
    if not list_info:
        return ''

    return f"{title_info}: {', '.join(list_info)}\n"

def add_info_to_tweet(total_tweet, info_to_add):
    """
    Add info to total_tweet (only if total len <= TWEET_LEN_LIMIT)

    Args:
        total_tweet (str): previous total tweet
        info_to_add (str): info to add to tweet

    Returns:
        str: total tweet
    """
    result_len = len(total_tweet) + len(info_to_add)

    if result_len <= TWEET_LEN_LIMIT:
        return total_tweet + info_to_add

    return total_tweet


def get_character_tweet_text(character_json):
    """
    Args:
        character_json (dict): character json objet

    Returns:
        str: text in format tweet
    """
    name = character_json['name']
    tweet_result = f"{name}\n\n"

    films = get_info_in_format("Films", character_json['films'])
    shortFilms = get_info_in_format("Short films", character_json['shortFilms'])
    tvShows = get_info_in_format("TV shows", character_json['tvShows'])
    videoGames = get_info_in_format("Videogames", character_json['videoGames'])

    total_info = [films, shortFilms, tvShows, videoGames]

    for info in total_info:
        tweet_result = add_info_to_tweet(tweet_result, info)

    return tweet_result


def get_character_url_image(character_json):
    """
    Args:
        character_json (dict): character json objet

    Returns:
        str: url image
    """
    return character_json.get('imageUrl', INVALID_URL_IMAGE)


def get_random_disney_character():
    """
    Returns:
        (tuple): tuple with len=2
        (character_tweet_text, character_url_image)
    """
    random_id = randint(0, MAX_CHARACTER_ID)

    url_character = f"{URL_CHARACTER}{random_id}"

    character_request = requests.get(url_character)

    try:
        character_json = character_request.json()
    except:
        return get_random_disney_character()

    character_tweet_text = get_character_tweet_text(character_json)
    character_url_image = get_character_url_image(character_json)

    return character_tweet_text, character_url_image