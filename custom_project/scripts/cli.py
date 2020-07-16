import click

from ..main import (_custom_function)
from ..utils import get_config, get_logger


@click.group(invoke_without_command=False)
@click.option('--config', type=click.Path(exists=True))
@click.pass_context
def cli(ctx, config):
    # read config and store in context
    cfg = get_config(config)
    ctx.ensure_object(dict)
    ctx.obj['CONFIG'] = cfg
    get_logger(cfg['log']['level'])

    # warn user in case there is no subcommand
    if ctx.invoked_subcommand is None:
        click.echo('custom_project module invoked without a subcommand...')


@cli.command()
@click.option('--argument', type=click.STRING)
@click.pass_context
def custom_function(ctx, argument):
    config = ctx.obj['CONFIG']

    _custom_function(config, argument)


if __name__ == '__main__':
    cli(obj={})
