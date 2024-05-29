import click

from praetorian_cli.handlers.chariot import chariot
from praetorian_cli.handlers.utils import Status, status_options, cli_handler


@chariot.group()
@cli_handler
def add(ctx):
    """Add a resource to Chariot"""
    pass


@add.command('seed')
@click.argument('seed', required=True)
@status_options(Status['seed'])
def assets(controller, seed, status, comment):
    """ Add a seed"""
    controller.add('seed', dict(dns=seed, status=status, comment=comment))


@add.command('file')
@click.argument('name')
@cli_handler
def upload(controller, name):
    """ Upload a file """
    controller.upload(name)


@add.command('webhook')
@cli_handler
def webhook(controller):
    """Add an authenticated URL for posting assets and risks"""
    response = controller.add_webhook()
    print(response)


def create_add_command(item_type, item_key_name, status_choices):
    @add.command(item_type, help=f"Add a {item_type}")
    @click.argument(item_key_name, required=True)
    @click.option('--key', required=True, help='Key of the related asset')
    @status_options(status_choices)
    @click.pass_context
    def command(controller, item_type, item_key, status, comment):
        controller.add(item_type, dict(key=item_key, status=status, comment=comment))


create_add_command('risk', 'name', Status['risk'])
create_add_command('job', 'capability', Status['job'])
