import paho.mqtt.publish as publish
import sys

broker_address = "test.mosquitto.org"
topic = "" ## put the topic of your choice

def publisher(message):
    publish.single(topic,message,hostname=broker_address)

if __name__ == "__main__":
    message = "hello there"
    publisher(message)
