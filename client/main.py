import time
from machine import Pin
from umqtt.robust import MQTTClient

led = Pin(13,Pin.OUT)
button = Pin(12,Pin.IN)
SECURED_ALARM = False

def sub_cb(topic, msg):
    if msg == b'on':
        led.value(1)
    elif msg == b'off':
        led.value(0)
    elif msg == b'activate':
        SECURED_ALARM == True
    elif msg == b'deactivate':
        SECURED_ALARM == False

c = MQTTClient("umqtt_client", "test.mosquitto.org")
c.connect()
c.DEBUG = True
c.set_callback(sub_cb)

if not c.connect(clean_session=False):
    print("New session being set up")
    c.subscribe(b"sum_topic")

def publish():
    if SECURED_ALARM:
        c.publish(b'sum_alarm','trigger')
        time.sleep(10)
    elif SECURED_ALARM == False:
        pass
    
    return True

button.irq(trigger=Pin.IRQ_RISING, handler= lambda t: publish())
while True:
    c.wait_msg()  

c.disconnect()
