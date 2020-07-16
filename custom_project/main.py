import logging

logger = logging.getLogger(__name__)


def _custom_function(config, argument):
    logger.debug(config)
    logger.debug(argument)

    logger.info('done!')
