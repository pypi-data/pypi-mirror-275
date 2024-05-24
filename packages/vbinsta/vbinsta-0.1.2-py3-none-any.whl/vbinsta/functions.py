from instagrapi import Client


def get_user_info(username: str) -> dict:
    pass


def upload_single_image(client: Client, path: str, caption: str) -> dict:
    client.photo_upload(path, caption)


def upload_carousel(client: Client, paths: list, caption: str) -> dict:
    pass
