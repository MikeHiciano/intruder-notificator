import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('data.db')
c = conn.cursor()

#TOD O LO RELACIONADO CON LOS TRIGGERS DEL ESP8266
class triggers():

	#CREAR TABLA TRIGGERS
	def create_triggers_table(self):
		c.execute("CREATE TABLE IF NOT EXISTS triggers (number INTEGER PRIMARY KEY ,device_mac TEXT,name TEXT,message TEXT,date TEXT)")

	#FUNCION PARA LA ENTRADA DE DATOS DE LOS TRIGGERS
	def trigger_data_entry(self,device_mac,name,message):
		with sqlite3.connect('data.db') as conn:
			c = conn.cursor()
			fecha = datetime.datetime.now()
			c.execute("INSERT INTO triggers(device_mac,name,message,date) VALUES(?,?,?,?)",(device_mac,name,message,fecha))
			conn.commit()
			return True

	#FUNCION PARA LEER TODOS LOS DATOS DE LA BASE DE DATOS DE LA TABLA TRIGGERS
	def read_triggers_data(self):
		with sqlite3.connect('data.db') as conn:
			c = conn.cursor()
			c.execute("SELECT * FROM triggers")
			for row in c.fetchall():
				print(row)
	
	def read_last_trigger_data(self,device_mac):
		with sqlite3.connect('data.db') as conn:
			c = conn.cursor()
			c.execute("SELECT * FROM triggers WHERE device_mac = ? ORDER BY device_mac DESC LIMIT 1",(device_mac))
			return c.fetchall()

class users():

	#CREAR TABLA USERS
	def create_user_table(self):
		c.execute("CREATE TABLE IF NOT EXISTS users(nombre TEXT,apellido TEXT,username TEXT,passwd TEXT,chat_id TEXT,device_mac TEXT,fecha TEXT)")
	
	#FUNCION PARA ENTRADA DE DATOS DE USUARIOS
	def user_data_entry(self,name,lastname,username,passwd,device_mac,chat_id):
		with sqlite3.connect('data.db') as conn:
			c = conn.cursor()
			fecha = str(datetime.datetime.now())
			c.execute("INSERT INTO users(nombre,apellido,username,passwd,device_mac,chat_id,fecha) VALUES(?,?,?,?,?,?,?)",(name,lastname,username,passwd,device_mac,chat_id,fecha))
			conn.commit()
	
	#FUNCION PARA LEER TODOS LOS DATOS DE LA TABLA USERS
	def read_users_data(self):
		with sqlite3.connect('data.db') as conn:
			c = conn.cursor()
			c.execute("SELECT * FROM users")
			return(c.fetchall())

	#FUNCION PARA LEER DATOS DE UN USUARIO EN ESPECIFICO
	def read_user_data(self,username):
		with sqlite3.connect('data.db') as conn:
			c = conn.cursor()
			c.execute("SELECT * FROM users WHERE username=?" %(str(username)))
			return(str(c.fetchall()))

	#FUNCION PARA BORRAR LOS DATOS UN USUARIO EN ESPECIFICO
	def delete_user_data(self,username):
		with sqlite3.connect('data.db') as conn:
			c = conn.cursor()
			c.execute("DELETE * FROM users WHERE username=?" %(username))
			conn.commit()
