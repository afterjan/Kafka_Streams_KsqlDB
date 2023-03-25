# Import libraries
from confluent_kafka import Consumer
import json

# Create the consumer instance.
c = Consumer({'bootstrap.servers':'localhost:9092','group.id':'python-consumer','auto.offset.reset':'earliest'})
print('Kafka Consumer has been initiated...')

c.subscribe(['SUBSBYTIME'])

def main():
    while True:
        msg = c.poll(1.0) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        print('Consumer: {}'.format(msg.value().decode('utf-8')))
    c.close()

if __name__ == '__main__':
    main()