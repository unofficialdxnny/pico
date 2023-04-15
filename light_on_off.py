import machine
import time

led_pin = machine.Pin(25, machine.Pin.OUT)

while True:
    # Turn on the LED
    led_pin.value(1)
    time.sleep(0.5)
    led_pin.value(0)
    time.sleep(0.5)
