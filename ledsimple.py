import machine
import time

# Define the pin that the LED is connected to
led_pin = machine.Pin(19, machine.Pin.OUT)

# Loop forever
while True:
    # Turn the LED on
    led_pin.value(1)
    
    # Wait for 1 second
    time.sleep(1)
    
    # Turn the LED off
    led_pin.value(0)
    
    # Wait for 1 second
    time.sleep(1)
