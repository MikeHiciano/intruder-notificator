import time
from machine import Pin
from umqtt.robust import MQTTClient

led = Pin(5,Pin.OUT)
button = Pin(4,Pin.IN,Pin.PULL_UP)

def sub_cb(topic, msg):
    if msg == b'bruh':
        led.value(1)
    else:
        led.value(0)

c = MQTTClient("umqtt_client", "test.mosquitto.org")
c.connect()
c.DEBUG = True
c.set_callback(sub_cb)

if not c.connect(clean_session=False):
    print("New session being set up")
    c.subscribe(b"sum_topic")

button.irq(trigger=Pin.IRQ_FALLING, handler= lambda t: c.publish(b'sum_alarm','trigger'))
while True:
    c.wait_msg()  

c.disconnect()
