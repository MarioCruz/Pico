import machine
import utime

# Configure the servo signal pin
servo_pin = machine.Pin(6, machine.Pin.OUT)
servo = machine.PWM(servo_pin)
servo.freq(10)

# Move servo to 0 degrees
servo.duty_u16(600)
print('0 degrees')
utime.sleep(3)


# Move servo to 180 degrees
servo.duty_u16(4400)
print('180  degrees')
utime.sleep(3)

# Move servo to 300 degrees
servo.duty_u16(5900)
print('300  degrees')
utime.sleep(3)

# Stop the PWM signal
servo.deinit()
