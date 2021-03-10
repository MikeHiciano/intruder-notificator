import os
import telepot
import sqlite3

bot = telepot.Bot(os.environ.get('API_KEY'))

class features():
    def send_message(name,message,device_mac):
        with sqlite3.connect('data.db') as conn:
            c = conn.cursor()
            c.execute("SELECT chat_id FROM users WHERE device_mac = ?",(device_mac,))
            response = c.fetchone()
            chat_id = (int(response[0]))
            bot.sendMessage(chat_id, '%s : %s' %(name,message))
    
