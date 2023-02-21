import machine
import time

# Define the pins that the LEDs are connected to
led1_pin = machine.Pin(16, machine.Pin.OUT)
led2_pin = machine.Pin(17, machine.Pin.OUT)
led3_pin = machine.Pin(19, machine.Pin.OUT)

# Create PWM objects for each LED
led1_pwm = machine.PWM(led1_pin)
led2_pwm = machine.PWM(led2_pin)
led3_pwm = machine.PWM(led3_pin)

# Set the PWM frequency for all LEDs
led1_pwm.freq(1000)
led2_pwm.freq(1000)
led3_pwm.freq(1000)

# Slowly dim the LEDs one at a time with a 3 second delay between them
led1_pwm.duty_u16(0)
led2_pwm.duty_u16(0)
led3_pwm.duty_u16(0)

print('led1')
for i in range(0, 65535, 32):
    led1_pwm.duty_u16(i)
    time.sleep(0.01)

time.sleep(3)

print('led2')
for i in range(0, 65535, 32):
    led2_pwm.duty_u16(i)
    time.sleep(0.01)

time.sleep(3)

print('led3')
for i in range(0, 65535, 32):
    led3_pwm.duty_u16(i)
    time.sleep(0.01)

time.sleep(3)

for i in range(65535, 0, -16):
    led1_pwm.duty_u16(i)
    time.sleep(0.001)

for i in range(65535, 0, -16):
    led2_pwm.duty_u16(i)
    time.sleep(0.001)

for i in range(65535, 0, -16):
    led3_pwm.duty_u16(i)
    time.sleep(0.001)


print('turn them off')
# Turn off all LEDs
led1_pwm.duty_u16(0)
led2_pwm.duty_u16(0)
led3_pwm.duty_u16(0)

