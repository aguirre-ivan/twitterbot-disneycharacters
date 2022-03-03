import requests
from os import remove


def create_image(url_image, image_name):
    """
    Create an image from url_image in image_name

    Args:
        url_image (str): image url
        image_name (str): save as image_name
    """
    f = open(image_name,'wb')
    response = requests.get(url_image)
    f.write(response.content)
    f.close()


def remove_image(image_name):
    """
    Remove image_name

    Args:
        image_name (str)
    """
    remove(image_name)