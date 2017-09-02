from __future__ import absolute_import

import logging
from django.core.management import BaseCommand

from app.tasks import adder

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--n', type=int, required=True, help="Number of messages to send"
        )

    def handle(self, *args, **options):
        num_msgs = options['n']

        for i in xrange(num_msgs):
            adder.delay(i, i)
            print i

        logger.info('{} messages sent'.format(num_msgs))
