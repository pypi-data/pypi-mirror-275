import base64
import json

import click

from praetorian_cli.handlers.chariot import chariot
from praetorian_cli.handlers.utils import cli_handler


@chariot.group()
@cli_handler
def get(ctx):
    """Get resource details from Chariot"""
    pass


@get.command('file')
@cli_handler
@click.argument('name')
def download(controller, name):
    """ Download a file """
    controller.download(name)


@get.command('report')
@cli_handler
@click.option('-name', '--name', help="Enter a risk name", required=True)
def report(controller, name):
    """ Generate definition for an existing risk """
    resp = controller.report(name=name)
    resp = base64.b64decode(resp).decode('utf-8')
    print(resp)


get_list = ['seeds', 'assets', 'risks', 'references', 'attributes', 'jobs', 'threats', 'files', 'accounts',
            'integrations']


def create_get_command(item):
    @get.command(item[:-1], help=f"Get {item[:-1]} details")
    @click.argument('key', required=True)
    @cli_handler
    def command(controller, key):
        resp = controller.my(dict(key=key))
        print(json.dumps(resp[item][0], indent=4))


for item in get_list:
    create_get_command(item)
