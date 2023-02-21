import utime
from machine import Pin

motor1a = Pin(2, Pin.OUT)
motor1b = Pin(3, Pin.OUT)

#Pump foward (out)
def foward():
   motor1a.high()
   motor1b.low()
   
#Pump Backward (into the reservoir)
def backward():
   motor1a.low()
   motor1b.high()

def stop():
   motor1a.low()
   motor1b.low()



foward()
utime.sleep(10)
backward()
utime.sleep(61)
#Incase I mess up
stop()
