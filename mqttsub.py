import paho.mqtt.client as mqtt
import sqlite3
import time
import re
from sqlite3 import Error

def create_connection(db_file):
	conn = None
	conn = sqlite3.connect(db_file)
	return conn

def sendToDB(data):
	print(data)
	data = re.split("/", data)
	print(data[0],data[1],data[2])
	db = "/home/userdb/Poseidon/Poseidon.db"
	conn = create_connection(db)
	c = conn.cursor()
	#query_db("INSERT INTO data_poseidon(Pression) VALUES (0)")
	c.execute("INSERT INTO data_poseidon(Pression, Humidity, Temperature) VALUES (" + data[0] + ", " + data[1] + ", " + data[2] +")")
	print("request done")
	conn.commit()
	conn.close()
	print("sent to db")

def on_connect(client, userdata, flags, rc):
	print("connected with code "+str(rc))
	client.subscribe("poseidon")

def on_message(client, userdata, msg):
	print(msg.payload.decode("utf-8"))
	sendToDB(msg.payload.decode("utf-8"))


client = mqtt.Client()
client.connect("192.168.1.42", 1883)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()

