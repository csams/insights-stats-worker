import logging
import yaml

from insights_messaging.consumers.rabbitmq import RabbitMQ

Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

log = logging.getLogger(__name__)


class Consumer(RabbitMQ):
    def deserialize(self, bytes_):
        return yaml.load(bytes_.decode("utf-8"), Loader=Loader)

    def get_url(self, msg):
        return msg["url"]
