import paho.mqtt.publish as publish
import sys

broker_address = "test.mosquitto.org"
topic = "sum_topic"

def publisher(message):
    publish.single(topic,message,hostname=broker_address)

if __name__ == "__main__":
    message = "hello there"
    publisher(message)