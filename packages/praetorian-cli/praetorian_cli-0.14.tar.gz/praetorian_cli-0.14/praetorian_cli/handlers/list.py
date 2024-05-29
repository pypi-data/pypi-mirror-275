import json

import click

from praetorian_cli.handlers.chariot import chariot
from praetorian_cli.handlers.utils import cli_handler


@chariot.group()
@cli_handler
def list(ctx):
    """Get a list of resources from Chariot"""
    pass


list_translate = {'seeds': 'seed', 'assets': 'asset', 'risks': 'risk', 'references': 'ref', 'attributes': 'attribute',
                  'jobs': 'job', 'threats': 'threat', 'files': 'file', 'accounts': 'account', 'integrations': 'account'}
list_filter = {'seeds': 'seed', 'assets': 'seed', 'risks': 'seed', 'references': 'seed', 'attributes': 'seed',
               'jobs': 'updated', 'threats': 'source', 'files': 'name', 'accounts': 'name', 'integrations': 'name'}


def create_list_command(item_type, item_filter):
    @list.command(item_type, help=f"List {item_type}")
    @click.option('--filter', help=f'Filter by {item_filter}', default="")
    @click.option('--offset', default="", help="list results from an offset")
    @click.option('--details', is_flag=True, default=False, help="Show detailed information")
    @cli_handler
    def command(controller, filter, offset, details):
        if item_type in ['accounts', 'integrations']:
            key = f'#{list_translate[item_type]}#{username(controller)}#{filter}'
        else:
            key = f'#{list_translate[item_type]}#{filter}'
        result = controller.my(dict(key=key, offset=offset))

        if item_type == 'integrations':
            result[item_type] = [
                item for item in result['accounts']
                if '@' not in item['key'].split("#")[-2]
            ]

        for hit in result.get(item_type, []):
            if details:
                print(json.dumps(hit, indent=4))
            else:
                print(f"{hit['key']}")

        if result.get('offset'):
            print(f"Offset: {json.dumps(result['offset'])}")


def username(controller):
    return controller.keychain.get().get(controller.keychain.profile, 'username')


for key, value in list_translate.items():
    create_list_command(key, list_filter[key])
