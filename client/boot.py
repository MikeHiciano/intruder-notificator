import network
import machine
import time

led = machine.Pin(2,machine.Pin.OUT)

sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)

sta_if.active(True)
sta_if.connect('<put your ssid>','<put your password>')

if sta_if.isconnected() == True:
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
