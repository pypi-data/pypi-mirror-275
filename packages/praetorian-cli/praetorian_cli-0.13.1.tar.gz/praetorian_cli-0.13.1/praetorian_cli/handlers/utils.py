import click

from enum import Enum
from functools import wraps
from praetorian_cli.sdk.chariot import Chariot


class Status(Enum):
    ACTIVE = "A"
    FROZEN = "F"
    UNKNOWN = "U"

    # job:status
    QUEUED = "JQ"
    RUNNING = "JR"
    FAIL = "JF"
    PASS = "JP"
    # risk:status
    OPEN = "O"
    OPEN_INFO = "OI"
    OPEN_LOW = "OL"
    OPEN_MEDIUM = "OM"
    OPEN_HIGH = "OH"
    OPEN_CRITICAL = "OC"
    REJECTED = "R"
    REJECTED_INFO = "RI"
    REJECTED_LOW = "RL"
    REJECTED_MEDIUM = "RM"
    REJECTED_HIGH = "RH"
    REJECTED_CRITICAL = "RC"
    CLOSED = "C"
    CLOSED_INFO = "CI"
    CLOSED_LOW = "CL"
    CLOSED_MEDIUM = "CM"
    CLOSED_HIGH = "CH"
    CLOSED_CRITICAL = "CC"
    TRIAGE = "T"
    TRIAGE_INFO = "TI"
    TRIAGE_LOW = "TL"
    TRIAGE_MEDIUM = "TM"
    TRIAGE_HIGH = "TH"
    TRIAGE_CRITICAL = "TC"


def handle_api_error(func):
    @wraps(func)
    def handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            click.secho(e.args[0], fg='red')

    return handler


@click.group()
@click.pass_context
def chariot(ctx):
    """ Chariot API access """
    ctx.obj = Chariot(keychain=ctx.obj)
