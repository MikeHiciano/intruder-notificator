from flask import Flask, request
import telegram

TOKEN = os.environ['TOKEN']
PORT = os.environ['PORT']
URL = os.environ['URL']
chat_id = int(os.environ['CHAT_ID'])

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route('/%s'%(TOKEN),methods=['POST'])
def response():

    update = telegram.Update.de_json(request.get_json(force=True),bot)
    chat_id = chat_id
    msg_id = update.message.message_id
    text = update.message.text.encode('utf-8').decode()
    print("new message: %s" %(text))

    if text == "/start":
        bot.sendMessage(chat_id=chat_id, 
                        text="SecuriBudge\r\nTo activate/deactivate the alarm use the command /alarm\r\nTo have your chat id use the command /id",
                        reply_to_message_id=msg_id)
    
    return 'ok'

@app.route('/set_webhook', methods=['GET','POST'])
def set_webhook():
    s = bot.setWebhook("%s:%s/bot%s" %(URL,PORT,TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook failed"

@app.route('/')
def index():
    return "works"

if __name__ == '__main__':
    app.run(threaded=True, debug=True,port=PORT)

