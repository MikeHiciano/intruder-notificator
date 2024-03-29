import logging
import threading
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import os
import time

TOKEN = os.environ.get('TOKEN')
PORT = int(os.environ.get('PORT', '8443'))
broker_address = os.environ.get('MQTT_ADDRESS')
broker_port = int(os.environ.get('MQTT_PORT'))
topic = os.environ.get('TOPIC')
subscriber_topic = os.environ.get('SUBSCRIBER_TOPIC')
chat_id_p = os.environ.get('CHAT_ID')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    kb = [[telegram.KeyboardButton('ON')],
          [telegram.KeyboardButton('OFF')]]
    kb_markup = telegram.ReplyKeyboardMarkup(kb)
    context.bot.sendMessage(chat_id=update.message.chat_id,
                    text="choose one: ",
                    reply_markup=kb_markup)

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def tel_id(update, context):
    update.message.reply_text("Your Telegram Chat ID is: \n%s" %(update.message.chat_id))

def echo(update, context):
    """Echo the user message."""
    if update.message.text == "ON":
        publish.single(topic,"on", hostname=broker_address,client_id='someone')
        update.message.reply_text("turning led ON")
        time.sleep(2)
    
    elif update.message.text == "OFF":
        publish.single(topic,"off", hostname=broker_address, client_id='someone')
        update.message.reply_text("turning led OFF")
        time.sleep(2)

def activate_alarm():
    publish.single(topic,"activate", hostname=broker_address, client_id='someone')
    update.message.reply_text("Alarm Armed")
    time.sleep(2)

def deactivate_alarm():
    publish.single(topic,"deactivate", hostname=broker_address, client_id='someone')
    update.message.reply_text("Alarm Disarmed")
    time.sleep(2)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def mqtt_subscriber(client,userdata,message):
    bot = telegram.Bot(TOKEN)

    if str(message.payload.decode("utf-8")) == "trigger":
        bot.send_message(chat_id=chat_id_p,text="Message From: %s\nMessage: Alarm Thriggered" %(message.topic))        

def mqtt_main():
    client = mqtt.Client()
    client.on_message = mqtt_subscriber
    client.connect(broker_address,broker_port,60)
    client.subscribe(subscriber_topic,0)
    client.loop_start()

def bot_main():
    """Start the bot."""
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("chatid", tel_id))
    dp.add_handler(CommandHandler("activate",activate_alarm))
    dp.add_handler(CommandHandler("deactivate",deactivate_alarm))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://intruder-notificator-test.herokuapp.com/' + TOKEN)
    updater.idle()

if __name__ == '__main__':
    mqtt_main()
    bot_main()
    
