from instagrapi.exceptions import TwoFactorRequired
import click
from instagrapi import Client

from .functions import upload_single_image
import os

USERNAME = os.getenv('INSTA_USERNAME')
PASSWORD = os.getenv('INSTA_PASSWORD')


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
    CODE = input("Enter the 2FA code: ")
    client.login(USERNAME, PASSWORD, verification_code=CODE)

    # Verify if the login was successful
    if client.user_id:
        print("Login successful!")
        if len(image) == 1:
            upload_single_image(client, image, 'Uploaded using vbinsta!')

    else:
        print("Login failed.")
