import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import threading
import os


#this part of the code is affected for the variables.sh script
broker_address = os.environ['BROKER_ADDRESS']
broker_port = int(os.environ['BROKER_PORT'])
topic = os.environ['MQTT_TOPIC']

bot_api_key = os.environ['BOT_API_KEY']
chat_id = int(os.environ['TELEGRAM_CHAT_ID'])
# ------------------------- end ------------------------------#

bot = telepot.Bot(bot_api_key)

#TELEGRAM BOT CLASS
class telegram_bot():
    
    def __init__(self):
        pass
    
    def handle(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type,chat_type, chat_id)

        command = msg['text']
        if content_type == 'text':
            if command == '/start':
                bot.sendMessage(chat_id,"SecuriBudge\r\nTo activate/deactivate the alarm use the command /alarm\r\nTo have your chat id use the command /id")
            
            elif command == '/alarm':
                keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [InlineKeyboardButton(text='Turn on', callback_data='on')],
                    [InlineKeyboardButton(text='Turn off', callback_data='off')]
                    ])

                bot.sendMessage(chat_id,"Alarm state: ", reply_markup=keyboard)
            
            elif command == '/id':
                bot.sendMessage(chat_id,"your chat id is: %s" %(chat_id))
            
            else:
                pass
        
    def callback_query(self,msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
        print('Callback query:', query_id, from_id, query_data)

        if query_data == 'on' or query_data == 'off':
            bot.answerCallbackQuery(query_id, text='the system is turned %s' %(query_data))
            if query_data == 'on':
                MESSAGE_VALUE = True

            elif query_data == 'off':
                MESSAGE_VALUE = False

    def run(self):
        try:
            bot = telepot.Bot(bot_api_key)
            answerer = telepot.helper.Answerer(bot)
            MessageLoop(bot,{'chat': self.handle,
                            'callback_query': self.callback_query}).run_as_thread()

            while True:
                time.sleep(1)

        except KeyboardInterrupt:
            print("turning off telegram bot server ...")

#MQTT SERVER CLASS

class mqtt_server():

    def __init__(self):
        pass

    def subscriber(self,client,userdata,message):
        print(topic,"=",str(message.payload.decode("utf-8")))
        if MESSAGE_VALUE == True:
            bot.sendMessage(chat_id,message.payload.decode("utf-8"))

        else:
            pass

    def run(self):
        try:
            client = mqtt.Client()
            client.on_message = self.subscriber
            client.connect(broker_address,broker_port,60)
            client.subscribe(topic,0)
            client.loop_forever()
        
        except KeyboardInterrupt:
            print("Turning off mqtt server...")

if __name__ == "__main__":

    print("Starting mqtt server ...")
    try:
        thread_1 = threading.Thread(target=mqtt_server().run)
        thread_2 = threading.Thread(target=telegram_bot().run)
        thread_1.start()
        thread_2.start()

    except KeyboardInterrupt:
        print("Bye ;)")
