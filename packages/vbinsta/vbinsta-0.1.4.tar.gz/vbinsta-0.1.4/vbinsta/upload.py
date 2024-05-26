import click
from instagrapi import Client

from .functions import login, upload_single_image, upload_carousel
import os

USERNAME = os.getenv('INSTA_USERNAME')
PASSWORD = os.getenv('INSTA_PASSWORD')

SESSION_FILE = os.path.expanduser("~/.vbinsta_session.json")


@click.command()
@click.option(
    '--image',
    '-i',
    required=True,
    type=click.Path(exists=True),
    multiple=True,
    help='Path to the image file to upload.'
)
def upload(image):
    client = Client()
    try:
        login(client, USERNAME, PASSWORD, SESSION_FILE)
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    # Verify if the login was successful
    if client.user_id:
        print("Login successful!")
        if len(image) == 1:
            upload_single_image(client, image[0], 'Uploaded using vbinsta!')
        if len(image) > 1:
            upload_carousel(client, image, 'Uploaded using vbinsta!')

    else:
        print("Login failed.")
