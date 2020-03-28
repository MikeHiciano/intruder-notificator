from umqtt.simple import MQTTClient
import machine
import time

server = b"test.mosquitto.org"
topic = b"" #put the same topic of your mqtt broker server
p1 = machine.Pin(5,machine.Pin.IN)
led = machine.Pin(16,machine.Pin.OUT)

def main(server,topic):
    c = MQTTClient(b"someone",server)
    c.connect()
    c.publish(topic,b"hello")
    c.disconnect()

while True:
    if p1.value() == True:
        led.off()
        main(server,topic)
        time.sleep(5)
        led.on()
