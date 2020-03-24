import paho.mqtt.client as mqtt
import telepot
from telepot.loop import MessageLoop as messageloop
import os

broker_address = os.environ['BROKER_ADDRESS']
broker_port = os.environ['BROKER_PORT']
topic = os.environ['MQTT_TOPIC']



def subscriber(client,userdata,message):
    print(topic,"=",message)

def main():
    try:
        client = mqtt.Client()
        client.on_message = subscriber
        client.connect(broker_address,broker_port,60)
        client.subscribe(topic,0)
        client.loop_forever()
    
    except KeyboardInterrupt:
        print("BYE ;)")
    
if __name__ == "main"

    print("Starting mqtt server ...")
    main()