#!/usr/bin/env python
"""
Kafka Producer.

Program to generate data to be send to Kafka
"""
from kafka import KafkaProducer
import json
from generate_data import create_instances
import time
import os


def data_serializer(message):
    """
    Serialize.

    function to serialize data
    """
    return json.dumps(message).encode('utf-8')


kafka = [os.environ['KAFKA_HOSTS']]
kafka_topic = os.environ['KAFKA_TOPIC']

producer = KafkaProducer(bootstrap_servers=kafka,
                         value_serializer=data_serializer,
                         acks='all',
                         retries=3)


if __name__ == '__main__':
    while True:
        instances_data = create_instances(num_devices=20, num_subnets=4)
        producer.send(kafka_topic, instances_data)
        time.sleep(10)
