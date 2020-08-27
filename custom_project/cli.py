########################################################################################################################
# IMPORTS

import logging

import click

from .utils import get_config, set_logger

########################################################################################################################
# COMMANDS

logger = logging.getLogger(__name__)


@click.group(invoke_without_command=False)
@click.option('--config', type=click.Path(exists=True))
@click.pass_context
def cli(ctx, config):
    # read config and store in context
    cfg = get_config(config)
    ctx.ensure_object(dict)
    ctx.obj['CONFIG'] = cfg
    set_logger(cfg['log']['level'])


@cli.command()
@click.option('--argument', type=click.STRING)
@click.pass_context
def custom_function(ctx, argument):
    config = ctx.obj['CONFIG']

    logger.debug(config)
    logger.debug(argument)

    logger.info('done!')


if __name__ == '__main__':
    cli(obj={})
