import requests
from os import remove


def create_image(url_image, image_name):
    f = open(image_name,'wb')
    response = requests.get(url_image)
    f.write(response.content)
    f.close()


def remove_image(image_name):
    remove(image_name)