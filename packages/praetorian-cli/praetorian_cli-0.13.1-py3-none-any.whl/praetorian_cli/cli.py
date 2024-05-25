import click

from praetorian_cli.handlers.account import chariot
from praetorian_cli.handlers.backend import chariot
from praetorian_cli.handlers.dnsdb import chariot
from praetorian_cli.sdk.keychain import Keychain


@click.group(invoke_without_command=True)
@click.version_option()
@click.pass_context
@click.option('--profile', default='United States', help='The keychain profile to use', show_default=True)
@click.option('--account', default=None, help='Run command as an account you belong to')
def cli(ctx, profile, account):
    ctx.obj = Keychain(profile=profile, account=account)
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


cli.add_command(chariot)

if __name__ == '__main__':
    cli()
