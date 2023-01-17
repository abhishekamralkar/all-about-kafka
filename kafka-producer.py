#!/usr/bin/env python
from kafka import KafkaProducer
import json
from generate_data import generate_data
import time, os

def data_serializer(message):
    return json.dumps(message).encode('utf-8')
    
kafka = [os.environ['KAFKA_HOSTS']]


#kafka = ['localhost:9092']
print(kafka)
producer = KafkaProducer(bootstrap_servers=kafka,
                         value_serializer=data_serializer,
                         acks='all',
                         retries = 3)

if __name__ == '__main__':
    while True:
        kafka_data = generate_data()
        producer.send('fakertopic', kafka_data)
        time.sleep(10)



# try:
#     future = producer.send('topic', b'From program')
#     record_metadata = future.get(timeout=60)
#     producer.flush()
# except KafkaError as exc:
#     print("Exception during getting assigned partitions - {}".format(exc))
#     # Decide what to do if produce request failed...
#     pass
# try:
#     print('Welcome to parse engine')
#     consumer = KafkaConsumer('test', bootstrap_servers='localhost:9092')
#     for message in consumer:
#         print(message)
# except Exception as e:
#     print(e)
#     # Logs the error appropriately. 
#     pass
