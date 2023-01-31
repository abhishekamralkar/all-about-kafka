#!/usr/bin/env python
"""Simple Kafka Consumer."""
from kafka import KafkaConsumer
import json
import os

kafka = [os.environ['KAFKA_HOSTS']]

if __name__ == '__main__':
    consumer = KafkaConsumer(
        "instance-info",
        bootstrap_servers=kafka,
        auto_offset_reset='earliest',
        group_id="instances-info-consumer-group")
    print("starting the consumer")
    for msg in consumer:
        print(f"Registered user = {json.loads(msg.value)}")
