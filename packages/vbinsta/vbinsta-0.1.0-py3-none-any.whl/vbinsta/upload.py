import click
from instagrapi import Client

from .functions import upload_single_image
import os

USERNAME = os.getenv('INSTA_USERNAME')
PASSWORD = os.getenv('INSTA_PASSWORD')


@click.command()
@click.option(
    '--path',
    '-p',
    required=True,
    type=click.Path(exists=True),
    help='Path to the image file to upload.'
)
def upload(path):
    client = Client()
    client.login(USERNAME, PASSWORD)

    upload_single_image(client, path, 'Uploaded using vbinsta!')
