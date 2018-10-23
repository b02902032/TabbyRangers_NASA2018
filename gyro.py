#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev2.motor import MediumMotor, OUTPUT_A, SpeedPercent, MoveTank, SpeedDPS
from ev3dev2.sensor import INPUT_1, INPUT_3
from ev3dev2.sensor.lego import GyroSensor #TouchSensor, 
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

from time import sleep


# Connect gyro and touch sensors to any sensor ports
gy = GyroSensor() 
#ts = TouchSensor()
sound = Sound()
m = MediumMotor(OUTPUT_A)

# Put the gyro sensor into ANGLE mode.
gy.mode = 'GYRO-ANG'
#gy.mode = 'GYRO-RATE'

while True:
    init_speed_sp = 10
    m.run_timed(time_sp=5000, speed_sp=init_speed_sp, stop_action='hold'); sleep(1)
    for i in range(10):
        init_speed_sp += 100
        m.run_timed(time_sp=5000, speed_sp=init_speed_sp); sleep(1)    
    for i in range(10):
        init_speed_sp -= 100
        m.run_timed(time_sp=5000, speed_sp=init_speed_sp); sleep(1)    
