#Python test code
#!/usr/bin/env pybricks-micropython
from cmath import pi
from pybricks.hub import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfaredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Ports, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

#initialize ev3
ev3 = EV3Brick()

#initialize motors
LMotor_1 = Motor(Port.A)
LMotor_2 = Motor(Port.B)
Gyro = GyroSensor(Port.1)

reset_angle(0)
while 