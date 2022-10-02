import shutil

import click
from bumpver.cli import update
from build.__main__ import main
from twine.commands.check import main as check
from twine.commands.upload import main as upload


@click.command()
@click.option('-u', '--username', prompt=True, envvar='TWINE_USERNAME')
@click.option('-p', '--password', prompt=True, envvar='TWINE_PASSWORD')
def update_to_pip(username: str, password: str):
    shutil.rmtree('dist', ignore_errors=True)
    update(['--patch'])
    main([])
    check(['dist/*'])
    upload([f'-u {username}', f'-p {password}', 'dist/*'])


if __name__ == '__main__':
    update_to_pip()
