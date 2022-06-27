## Flink Aggregate Application

This application is created to learn how Flink Aggregation works.


### Kafka
Kafka topics are used to read and write data from. 
There are two kafka streams
- input-kafka-topic
- output-kafka-topic

Kafka runs on docker. Use `docker-compose up` in the `01-kafka` directory to get everything up and running.


### Python Producer
A python program generates random clickstream data.
It pushes the data into the kafka topic `input-kafka-topic`.


## Flink App
- Read data from the `input-kafka-topic`.
- Aggregate the data in realtime for every 60 seconds.
- Write the data into the `output-kafka-topic`.