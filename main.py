from machine import Pin, PWM
from time import sleep

# Define motor pins
IN1 = Pin(9, Pin.OUT)
IN2 = Pin(8, Pin.OUT)
IN3 = Pin(10, Pin.OUT)
IN4 = Pin(11, Pin.OUT)

ENA = PWM(Pin(8))  # PWM pin for motor A (e.g., GPIO 6)
ENB = PWM(Pin(11))  # PWM pin for motor B (e.g., GPIO 7)

# Define sensor pins
leftmost_sensor = Pin(1,Pin.IN)
left_sensor = Pin(2, Pin.IN)
center_sensor = Pin(3,Pin.IN)
right_sensor = Pin(4, Pin.IN)
rightmost_sensor = Pin(5,Pin.IN)

ENA.freq(1000)  # 1 kHz frequency for motor A
ENB.freq(1000)  # 1 kHz frequency for motor B

def set_motor_speeds(speed_a, speed_b):
    ENA.duty_u16(int(speed_a * 65535))  # Convert speed (0-1) to duty cycle (0-65535)
    ENB.duty_u16(int(speed_b * 65535))  # Convert speed (0-1) to duty cycle (0-65535)


def forward(speed=0.4):
    set_motor_speeds(speed, speed)
    IN1.value(1)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)

def turn_left(speed=0.3):
    set_motor_speeds(speed, speed)
    IN1.value(0)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)

def turn_right(speed=0.3):
    set_motor_speeds(speed, speed)
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)

def sharp_left(speed=0.6):
    set_motor_speeds(speed, speed)
    IN1.value(0)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)

def sharp_right(speed=0.6):
    set_motor_speeds(speed, speed)
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)

def stop():
    set_motor_speeds(0, 0)
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)
  
while True:
    leftmost_value = leftmost_sensor.value()
    left_value = left_sensor.value()
    center_value = center_sensor.value()
    right_value = right_sensor.value()
    rightmost_value = rightmost_sensor.value()
    if leftmost_value == 0 and left_value == 0 and center_value == 1 and right_value == 0 and rightmost_value == 0:
        forward(0.4)  # Move forward at 60% speed
    elif leftmost_value == 0 and left_value == 1 and center_value == 1 and right_value == 0 and rightmost_value == 0:
        turn_left(0.3)
        
        # Slight left turn at 50% speed       
    elif leftmost_value == 1 and left_value == 1 and center_value == 0 and right_value == 0 and rightmost_value == 0:
        sharp_left(0.6)
        
        # Sharp left turn at 50% speed
    elif leftmost_value == 0 and left_value == 0 and center_value == 1 and right_value == 1 and rightmost_value == 0:
        turn_right(0.3)
        
        # Slight right turn at 50% speed
    elif leftmost_value == 0 and left_value == 0 and center_value == 0 and right_value == 1 and rightmost_value == 1:
        sharp_right(0.6)
        
        # Sharp right turn at 50% speed
    elif leftmost_value == 0 and left_value == 0 and center_value == 0 and right_value == 0 and rightmost_value == 0:
        stop()  # Stop if no line is detected
    elif leftmost_value == 1 and left_value == 1 and center_value == 1 and right_value == 1 and rightmost_value == 1:
        stop()  # Stop if no line is detected
    elif leftmost_value == 1 and left_value == 0 and center_value == 0 and right_value == 0 and rightmost_value == 0:
        sharp_left(0.6)
        
        # Stop if no line is detected
    elif leftmost_value == 0 and left_value == 0 and center_value == 0 and right_value == 0 and rightmost_value == 1:
        sharp_right(0.6)
        
        # Stop if no line is detected
    elif leftmost_value == 1 and left_value == 1 and center_value == 1 and right_value == 0 and rightmost_value == 0:
        turn_left(0.3)
        
        # Stop if no line is detected
    elif leftmost_value == 0 and left_value == 0 and center_value == 1 and right_value == 1 and rightmost_value == 1:
        turn_right(0.3)     
        # Stop if no line is detected
    elif leftmost_value == 0 and left_value == 1 and center_value == 1 and right_value == 1 and rightmost_value == 0:
         forward(0.4)
    elif leftmost_value == 0 and left_value == 1 and center_value == 0 and right_value == 0 and rightmost_value == 0:
         turn_left(0.3)         
    elif leftmost_value == 0 and left_value == 0 and center_value == 0 and right_value == 1 and rightmost_value == 0:
         turn_right(0.3)
         
    elif leftmost_value == 1 and left_value == 1 and center_value == 1 and right_value == 1 and rightmost_value == 0:
         turn_left(0.3)
         
    elif leftmost_value == 0 and left_value == 1 and center_value == 1 and right_value == 1 and rightmost_value == 1:
         turn_right(0.3)
         
    else:
         stop()
        
      # Default action if the robot is on the line
