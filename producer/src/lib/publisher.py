from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import json
import os
import time

topic = os.environ.get('PCDEMO_CHANNEL') or 'stats'

class Publisher:

    def __init__(self, logger):
        self.logger = logger
        while not hasattr(self, 'producer'):
            try:
                self.producer = KafkaProducer(bootstrap_servers=["kafka:9092"])
            except NoBrokersAvailable as err:
                self.logger.error("Unable to find a broker: {0}".format(err))
                time.sleep(1)

    def push(self, message):
        self.logger.debug("Publishing: {0}".format(message))
        try:
            if self.producer:
                self.producer.send(topic, json.dumps(message))
        except AttributeError:
            self.logger.error("Unable to send {0}. The producer does not exist.".format(message))
