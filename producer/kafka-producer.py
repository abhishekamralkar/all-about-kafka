#!/usr/bin/env python
"""
Kafka Producer.

Program to generate data to be send to Kafka
"""
from kafka import KafkaProducer
import json
from generate_data import created_instances
import time
import os


def data_serializer(message):
    """
    Serialize.

    function to serialize data
    """
    return json.dumps(message).encode('utf-8')


kafka = [os.environ['KAFKA_HOSTS']]


producer = KafkaProducer(bootstrap_servers=kafka,
                         value_serializer=data_serializer,
                         acks='all',
                         retries=3)

if __name__ == '__main__':
    while True:
        instances_data = created_instances(num_devices=20, num_subnets=4)
        producer.send('instance-info', instances_data)
        time.sleep(10)
