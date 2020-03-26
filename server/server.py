import paho.mqtt.client as mqtt
import telepot
from telepot.loop import MessageLoop
import os
import threading

broker_address = os.environ['BROKER_ADDRESS']
broker_port = int(os.environ['BROKER_PORT'])
topic = os.environ['MQTT_TOPIC']

bot_api_key = os.environ['BOT_API_KEY']
chat_id = int(os.environ['CHAT_ID'])

bot = telepot.Bot(bot_api_key)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type,chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id,msg['text'])

def subscriber(client,userdata,message):
    print(topic,"=",str(message.payload.decode("utf-8")))
    bot.sendMessage(chat_id,message.payload.decode("utf-8"))

def mqtt_thread():

    client = mqtt.Client()
    client.on_message = subscriber
    client.connect(broker_address,broker_port,60)
    client.subscribe(topic,0)
    client.loop_forever()
    
def telepot_thread():
    MessageLoop(bot,handle).run_as_thread()

if __name__ == "__main__":
    comm = threading.Thread(target=mqtt_thread)
    message = threading.Thread(target=telepot_thread)
    print("Starting mqtt server ...")
    try:
        comm.start()
        message.start()

    except KeyboardInterrupt:
        print("Bye ;)")
