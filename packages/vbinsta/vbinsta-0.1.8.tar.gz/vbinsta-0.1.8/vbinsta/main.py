import click
from .upload import upload

CONTEXT_SETTINGS = dict(
    help_option_names=[
        '-h',
        '--help'
    ],
    auto_envvar_prefix='VBINSTA'
)


@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    pass


main.add_command(upload)
