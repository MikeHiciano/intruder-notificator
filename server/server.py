import paho.mqtt.client as mqtt
import telepot
from telepot.loop import MessageLoop
import os


#this part of the code is affected for the variables.sh script
broker_address = os.environ['BROKER_ADDRESS']
broker_port = int(os.environ['BROKER_PORT'])
topic = os.environ['MQTT_TOPIC']

bot_api_key = os.environ['BOT_API_KEY']
chat_id = int(os.environ['CHAT_ID'])

# ------------------------- end ------------------------------#

bot = telepot.Bot(bot_api_key)

#TELEGRAM BOT FUNCTION
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type,chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id,msg['text'])

#MQTT SUBSCRIBER FUNCTION
def subscriber(client,userdata,message):
    print(topic,"=",str(message.payload.decode("utf-8")))
    bot.sendMessage(chat_id,message.payload.decode("utf-8"))

def mqtt_main():

    client = mqtt.Client()
    client.on_message = subscriber
    client.connect(broker_address,broker_port,60)
    client.subscribe(topic,0)
    client.loop_forever()
    
def telepot_main():
    MessageLoop(bot,handle).run_as_thread()

if __name__ == "__main__":

    print("Starting mqtt server ...")
    try:
        mqtt_main()
        telepot_main()

    except KeyboardInterrupt:
        print("Bye ;)")
