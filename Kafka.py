import json
import uuid

from kafka3 import KafkaProducer, KafkaConsumer, TopicPartition


class Kafka:
    def __init__(self, topic):
        self.kafka_bootstrap_server = 'kafka-1:19092' 
        self.kafka_topic = topic
        self.kafka_offset_reset = 'earliest' # might have to change to latest
        self.topic_partition = TopicPartition(self.kafka_topic, 0)

    producer: KafkaProducer
    consumer: KafkaConsumer

    def close(self):
        self.producer.close()
        self.consumer.close()


class KafkaWriter(Kafka):
    def __init__(self, topic):
        super(KafkaWriter, self).__init__(topic)
        try:
            self.producer = KafkaProducer(
                bootstrap_servers=self.kafka_bootstrap_server,
                key_serializer=str.encode,
                value_serializer=lambda v: json.dumps(v).encode('utf-8'))

        except ValueError as ve:
            # might hapen when the bootstrap server is unreachable
            print(f'  !!! error while creating kafka producer: {ve}')

    def store(self, message_key: str, data: json) -> None:
        if self.producer is not None:
            self.producer.send(self.kafka_topic, key=message_key, value=data)
            self.producer.flush()


class KafkaReader(Kafka):
    def __init__(self, topic):
        super(KafkaReader, self).__init__(topic)

        try:
            self.consumer = KafkaConsumer(
                bootstrap_servers=self.kafka_bootstrap_server,
                group_id=uuid.uuid4().hex,
                client_id=uuid.uuid4().hex,
                auto_offset_reset='earliest', # changed it from self.auto_offset_reset
                enable_auto_commit=True,

                key_deserializer=lambda k: k.decode('utf-8'),
                value_deserializer=lambda m: json.loads(m.decode('utf-8'))
            )
        except ValueError as ve:
            # might hapen when the bootstrap server is unreachable
            print(f'  !!! error while creating kafka consumer: {ve}')
        if self.consumer is not None:
            self.consumer.assign([self.topic_partition])

    def retrieve(self) -> {}:
        predictions = []
        if self.consumer is not None:
            while True:  # poll until the size of returned messages is zero, then break the loop
                messages = self.consumer.poll(timeout_ms=3000)
                if len(messages) == 0:
                    # no more messages in topic
                    break

                for key in messages.keys():
                    records = messages[key]
                    for record in records:
                        predictions.append(record.value)
        return predictions
