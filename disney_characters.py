import requests
from random import randint

MAX_CHARACTER_ID = 7526
TWEET_LEN_LIMIT = 280

INVALID_URL_IMAGE = -1
URL_CHARACTER = 'https://api.disneyapi.dev/characters/'


def get_info_in_format(character_json, name_info):
    info = character_json[name_info]
    info = info if len(info) != 0 else ['None']
    return ','.join(info)


def get_character_info(character_json):
    name = character_json['name']

    films = get_info_in_format(character_json, 'films')
    tvShows = get_info_in_format(character_json, 'tvShows')
    videoGames = get_info_in_format(character_json, 'videoGames')

    text_info = f"{name}\n\nFilms: {films}\nTV Shows: {tvShows}"

    videoGamesTitle = 'VideoGames: '

    # Video games are not very relevant
    has_correct_lenght = (len(text_info) + len(videoGames) + len(videoGamesTitle) + 1) <= TWEET_LEN_LIMIT# +1 = \n

    if videoGames != 'None' and has_correct_lenght:
        text_info += f"\n{videoGamesTitle}{videoGames}"

    return text_info


def get_character_url_image(character_json):
    return character_json.get('imageUrl', INVALID_URL_IMAGE)


def get_random_disney_character():
    random_id = randint(0, MAX_CHARACTER_ID)

    url_character = f"{URL_CHARACTER}{random_id}"

    character_request = requests.get(url_character)

    try:
        character_json = character_request.json()
    except:
        return get_random_disney_character()

    character_info = get_character_info(character_json)
    character_url_image = get_character_url_image(character_json)

    return character_info, character_url_image