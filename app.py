import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import paho.mqtt.publish as publish
import os

TOKEN = os.environ.get('TOKEN')
PORT = int(os.environ.get('PORT', '8443'))
broker_address = os.environ.get('MQTT_ADDRESS')
topic = os.environ.get('TOPIC')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    kb = [[telegram.KeyboardButton('ON')],
          [telegram.KeyboardButton('OFF')]]
    kb_markup = telegram.ReplyKeyboardMarkup(kb)
    updater.bot.sendMessage(chat_id=update.message.chat_id,
                    text="choose one: ",
                    reply_markup=kb_markup)

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(update, context):
    """Echo the user message."""
    if update.message.text == "ON":
        publish.single(topic,"bruh", hostname=broker_address,client_id='someone')
        update.message.reply_text("turning led ON")
    
    elif update.message.text == "OFF":
        publish.single(topic,"something", hostname=broker_address, client_id='someone')
        update.message.reply_text("turning led OFF")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)

    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://intruder-notificator-test.herokuapp.com/' + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()
