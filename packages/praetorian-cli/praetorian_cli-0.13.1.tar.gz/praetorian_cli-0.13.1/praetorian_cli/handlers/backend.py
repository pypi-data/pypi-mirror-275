import json
import os
import click

from praetorian_cli.handlers.utils import Status
from praetorian_cli.handlers.utils import chariot
from praetorian_cli.handlers.utils import handle_api_error

get_options = {
    'seeds': 'seed',
    'assets': 'asset',
    'attributes': 'attribute',
    'risks': 'risk',
    'jobs': 'job',
    'threats': 'threat',
    'files': 'file',
    'references': 'ref'
}


@chariot.command('get')
@click.pass_obj
@handle_api_error
@click.argument('type', type=click.Choice(get_options.keys()), required=True)
@click.option('-seed', '--seed', default="",
              help="Filter Assets, Risks, Seeds, Attributes or References by seed domain")
@click.option('-updated', '--updated', default="", help="Filter Jobs by updated date")
@click.option('-source', '--source', type=click.Choice(['KEV']), default="KEV", help="Filter Threats by source")
@click.option('-name', '--name', default="", help="Filter Files by relative path")
@click.option('-offset', '--offset', default="", help="Get results from an offset")
def get(controller, type, seed, updated, source, name, offset):
    """ Get all assets, seeds, risks, jobs, threats, or files """
    if seed != "":
        key = seed  # Seeds are tied to attributes now, so return those instead
        type = "attributes"
    elif type == 'jobs':
        key = f'#{get_options[type]}#{updated}'
    elif type == 'threats':
        key = f'#{get_options[type]}#{source}'
    elif type == 'files':
        key = f'#{get_options[type]}#{name}'
    else:
        key = f'#{get_options[type]}#{seed}'

    result = controller.my(dict(key=key, offset=offset))
    for hit in result.get(type, []):
        print(f"{hit['key']}")
    if result.get('offset'):
        print(f"Offset: {json.dumps(result['offset'])}")


@chariot.command('add')
@click.pass_obj
@handle_api_error
@click.argument('resource', type=click.Choice(['risk', 'seed', 'job', 'attribute']), required=True)
@click.argument('name')
@click.option('-key', '--key', help="Asset key for adding a risk, job, or attribute")
@click.option('-status', '--status', type=click.Choice([s.value for s in Status]), required=False,
              help="Status of the object")
@click.option('-comment', '--comment', default="", help="Add a comment")
@click.option('-class', '--class', 'clss', default="", help="Attribute class")
def add(controller, resource, name, key, status, comment, clss):
    """ Add a risk, seed, job, or attribute """
    if resource == 'risk' or resource == 'job':
        if not key:
            raise click.BadParameter('Asset key is required for adding a risk or job".')
        controller.add(resource, dict(key=key, name=name, status=status, comment=comment))
    if resource == 'seed':
        controller.add(resource, dict(dns=name, status=status, comment=comment))
    if resource == 'attribute':
        controller.add('asset/attribute', {'class': clss, 'key': key, 'name': name})


@chariot.command('delete')
@click.pass_obj
@handle_api_error
@click.argument('resource', type=click.Choice(['seed', 'attribute']), required=True)
@click.argument('key')
def delete_seed(controller, resource, key):
    """ Delete any seed or attribute """
    if resource == 'attribute':
        controller.delete('asset/attribute', key)
    else:
        controller.delete(resource, key)


@chariot.command('update')
@click.pass_obj
@handle_api_error
@click.argument('resource', type=click.Choice(['asset', 'risk', 'seed']), required=True)
@click.argument('key', required=True)
@click.option('-status', '--status', type=click.Choice([s.value for s in Status]), required=False, default="AS")
@click.option('-comment', '--comment', help="Add a comment")
def update(controller, resource, key, status, comment=''):
    """ Update an asset, risk, or seed """
    controller.update(resource, dict(key=key, status=status, comment=comment))


@chariot.command('upload')
@click.pass_obj
@handle_api_error
@click.argument('name')
def upload(controller, name):
    """ Upload a file """
    controller.upload(name)


@chariot.command('download')
@click.pass_obj
@handle_api_error
@click.argument('key')
@click.argument('path')
def download(controller, key, path):
    """ Download any previous uploaded file """
    controller.download(key, path)


@chariot.command('search')
@click.pass_obj
@handle_api_error
@click.option('-term', '--term', help="Enter a search term", required=True)
@click.option('-count', '--count', is_flag=True, help="Return statistics on search")
def search(controller, term="", count=False):
    """ Query the data store for arbitrary matches """
    if count:
        print(controller.count(dict(key=term)))
    else:
        resp = controller.my(dict(key=term))
        for key, value in resp.items():
            if isinstance(value, list):
                for hit in value:
                    print(f"{hit['key']}")


@chariot.command('report')
@click.pass_obj
@handle_api_error
@click.option('-name', '--name', help="Enter a risk name", required=True)
def report(controller, name=""):
    """ Generate definition for an existing risk """
    resp = controller.report(name=name)
    print(resp)


@chariot.command('test')
@click.pass_obj
@click.option('-suite', '--suite', type=click.Choice(["coherence"]), help="Run a specific test suite")
@click.argument('key', required=False)
def trigger_all_tests(controller, key, suite):
    """ Run integration test suite """
    try:
        import pytest
    except ModuleNotFoundError:
        print("Install pytest using 'pip install pytest' to run this command")
    test_directory = os.path.relpath("praetorian_cli/sdk/test", os.getcwd())
    os.environ['CHARIOT_PROFILE'] = controller.keychain.profile
    command = [test_directory]
    if key:
        command.extend(['-k', key])
    if suite:
        command.extend(['-m', suite])
    pytest.main(command)
