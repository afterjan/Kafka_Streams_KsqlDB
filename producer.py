from confluent_kafka import Producer
import json
import logging
from csv import DictReader
import time

# create the producer by specifying the port of Kafka cluster
p = Producer({'bootstrap.servers':'localhost:9092'})
print('Kafka Producer has been initiated...')

def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        print(message)

topic_name = 'bankmarketing'

def main():
    with open('bank_marketing_dataset20.csv', 'r') as file:
        data = DictReader(file)
        for cust in data:
            p.produce(topic_name, json.dumps(cust).encode('utf-8'), callback=receipt)
            p.poll(1)
            p.flush()
            time.sleep(3)

if __name__ == '__main__':
    main()
