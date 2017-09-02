from __future__ import absolute_import

import logging
from uuid import uuid4

from django.conf import settings
from django.core.management import BaseCommand
from google.cloud import pubsub_v1


logger = logging.getLogger(__name__)

batch_settings = pubsub_v1.types.BatchSettings(**settings.batch_settings_options)
publisher = pubsub_v1.PublisherClient(batch_settings)
topic_path = publisher.topic_path(project, topic_name)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--n', type=int, required=True, help="Number of messages to send"
        )

    def handle(self, *args, **options):
        num_msgs = options['n']

        for i in xrange(num_msgs):
            data = u'Message number {0}: {1}'.format(i, uuid4())
            data = data.encode('utf-8')
            publisher.publish(topic_path, data=data)

        logger.info('{} messages sent'.format(num_msgs))
