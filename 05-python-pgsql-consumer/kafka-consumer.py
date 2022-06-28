from pydoc_data.topics import topics
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
 bootstrap_servers='localhost:9092',
 value_deserializer = lambda v: json.loads(v.decode('ascii'))
)

consumer.subscribe(topics = 'input-kafka-topic')

for message in consumer:
    print (message.value)