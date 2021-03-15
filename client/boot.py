import time
import micropython
import machine
import network
import esp

esp.osdebug(None)
import gc
gc.collect()

ssid = '< put your ssid>'
password = '< put your password>'

led = machine.Pin(2,machine.Pin.OUT)

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid,password)

if station.isconnected() == True:
    for i in range(2):
        led.off()
        time.sleep(1)
        led.on()
        time.sleep(1)

else:
    for i in range(3):
        led.off()
        time.sleep(0.5)
        led.on()
        time.sleep(0.5)
