""" This module is triggered by a cron job. """

import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def run(event, context):
    """This function is triggered by a cron job."""
    current_time = datetime.datetime.now().time()
    logger.info("Your cron function ran at %s", str(current_time))
