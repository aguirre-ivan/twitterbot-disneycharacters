import requests
from random import randint

MAX_CHARACTER_ID = 7526
URL_CHARACTER = 'https://api.disneyapi.dev/characters/'


def get_character_info(character_json):
    films = character_json['films']
    tvShows = character_json['tvShows']

    films = films if len(films) != 0 else ['None']
    tvShows = tvShows if len(tvShows) != 0 else ['None']

    text_info = f"Films: {','.join(films)}\nTV Shows: {','.join(tvShows)}"

    return text_info


def get_character_url_image(character_json):
    return character_json['imageUrl']


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