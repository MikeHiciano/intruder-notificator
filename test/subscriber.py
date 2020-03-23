import paho.mqtt.client as mqtt

broker_address = "test.mosquitto.org"
broker_port = 1883
topic = "sum_topic"


def on_message(client,userdata,message):
    print(topic ," = ", str(message.payload.decode("utf-8")))

if __name__ == "__main__":
    try:
        client = mqtt.Client()
        client.on_message = on_message
        client.connect(broker_address,broker_port,60)
        client.subscribe(topic,0)
        client.loop_forever()

    except KeyboardInterrupt:
        print("BYE ;)") 