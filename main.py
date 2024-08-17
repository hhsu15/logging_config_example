import logging
import logging.config

logging.config.fileConfig("mylogging.conf")
logger = logging.getLogger(__file__)
logger.debug("TEST")
